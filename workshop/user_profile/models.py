from django.core.validators import MinLengthValidator
from django.db import models
from workshop.helpers.validators import validate_only_letters, validate_min_year, validate_max_year


class Profile(models.Model):

    MALE, FEMALE, DO_NOT_SHOW = 'Male', 'Female', 'Do Not Show'

    CHOICES = (
        (MALE, MALE),
        (FEMALE, FEMALE),
        (DO_NOT_SHOW, DO_NOT_SHOW),
    )

    first_name = models.CharField(
        max_length=30,
        validators=(
            MinLengthValidator(2),
            validate_only_letters,
        )
    )

    last_name = models.CharField(
        max_length=30,
        validators=(
            MinLengthValidator(2),
            validate_only_letters,
        )
    )

    picture = models.URLField()

    date_of_birth = models.DateField(
        null=True,
        blank=True,
        validators=(
            validate_min_year,
            validate_max_year,
        )
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    email = models.EmailField(
        null=True,
        blank=True,
    )

    gender = models.CharField(
        null=True,
        blank=True,
        max_length=max([len(x) for (_, x) in CHOICES]),
        choices=CHOICES,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
