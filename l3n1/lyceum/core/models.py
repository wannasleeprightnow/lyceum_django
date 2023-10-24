from django.core.validators import MinValueValidator
from django.db.models import AutoField, BooleanField, CharField, Model


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

    class Meta:
        abstract = True
