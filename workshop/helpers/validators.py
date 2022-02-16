import datetime

from django.core.exceptions import ValidationError


def validate_only_letters(value):

    for ch in value:

        if not ch.isalpha():
            raise ValidationError('Field must consist only of letters!')


def validate_file_size(value):
    limit = 5 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 5 MiB.')


def validate_min_year(value):
    if value.year < datetime.date(1920, 1, 1).year:
        raise ValidationError('Date of birth cannot be earlier that 01.01.1920!')


def validate_max_year(value):
    if value > datetime.datetime.now().date():
        raise ValidationError('Date of birth cannot be in the future!')
