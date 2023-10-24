import re

from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible


def perfect_validator(value):
    pattern = re.compile(r'(?:\bроскошно\b|\bпревосходно\b)', re.IGNORECASE)
    if not re.search(pattern, value):
        raise ValidationError('Нет `превосходно` или `роскошно`')


@deconstructible
class ValidateMustContain(BaseValidator):
    def __init__(self, *args):
        self.words = args

    def __call__(self, value):
        if not any(
            map(
                lambda word: re.search(
                    re.compile(r'(?:\b' + word + r'\b)', re.IGNORECASE), value
                ),
                tuple(self.words),
            ),
        ):
            raise ValidationError('В тексте нет требуемых слов.')

    def __eq__(self, other):
        return self.foo == other.foo
