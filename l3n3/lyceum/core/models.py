from re import compile

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db.models import AutoField, BooleanField, CharField, Model
from transliterate import translit
from transliterate.exceptions import LanguageDetectionError

ONLY_LETTERS_REGEX = compile(r'[^\w]')


class AbstractModel(Model):
    id = AutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='id',
        validators=[MinValueValidator(1)],
    )
    is_published = BooleanField(
        verbose_name='опубликовано',
        help_text='Опубликован ли товар?',
        default=True,
    )
    name = CharField(
        verbose_name='название',
        help_text='Введите название товара',
        max_length=150,
        unique=True,
    )
    canonical_name = CharField(
        verbose_name='каноническое название',
        help_text='Каноническое название элемента',
        max_length=150,
        null=True,
        unique=True,
        editable=False,
    )

    def _generate_canonical_name(self):
        try:
            transliterated = translit(
                self.name.lower(),
                reversed=True,
            )
        except LanguageDetectionError:
            transliterated = self.name.lower()

        return ONLY_LETTERS_REGEX.sub('', transliterated)

    def save(self, *args, **kwargs):
        self.canonical_name = self._generate_canonical_name()
        super().save(*args, **kwargs)

    def clean(self):
        self.canonical_name = self._generate_canonical_name()
        if (
            type(self)
            .objects.filter(canonical_name=self.canonical_name)
            .exclude(id=self.id)
            .count()
            > 0
        ):
            raise ValidationError('Такой элемент уже существует')

    class Meta:
        abstract = True
