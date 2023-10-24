import re

from django.core.exceptions import ValidationError
from django.core.validators import (
    MaxValueValidator,
    MinValueValidator,
)
from django.db.models import (
    CASCADE,
    ForeignKey,
    IntegerField,
    ManyToManyField,
    SlugField,
    TextField,
)

from core.models import AbstractModel


def perfect_validator(value):
    pattern = re.compile(r'(?:\bроскошно\b|\bпревосходно\b)', re.IGNORECASE)
    if not re.search(pattern, value):
        raise ValidationError('Нет `превосходно` или `роскошно`')


class Tag(AbstractModel):
    slug = SlugField(
        verbose_name='слаг',
        help_text='Введите слаг',
        max_length=200,
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'catalog_tag'
        verbose_name = 'тег'
        verbose_name_plural = 'теги'


class Category(AbstractModel):
    slug = SlugField(
        verbose_name='слаг',
        help_text='Введите слаг',
        max_length=200,
    )
    weight = IntegerField(
        verbose_name='вес',
        help_text='Введите вес',
        default=100,
        validators=[MinValueValidator(1), MaxValueValidator(32767)],
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'catalog_category'
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Item(AbstractModel):
    category = ForeignKey(
        Category,
        verbose_name='категория',
        help_text='Выберите категорию',
        on_delete=CASCADE,
        null=True,
    )
    tags = ManyToManyField(
        Tag, verbose_name='теги', help_text='Выберите теги.'
    )
    text = TextField(
        verbose_name='текст',
        help_text='Введите текст',
        validators=[perfect_validator],
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'catalog_item'
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
