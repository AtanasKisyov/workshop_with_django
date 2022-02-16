import datetime

from django.db import models

from workshop.helpers.validators import validate_min_year, validate_max_year
from workshop.user_profile.models import Profile


class Pet(models.Model):

    CAT, DOG, BUNNY, PARROT, FISH, OTHER = 'Cat', 'Dog', 'Bunny', 'Parrot', 'Fish', 'Other'

    CHOICES = (
        (CAT, CAT),
        (DOG, DOG),
        (BUNNY, BUNNY),
        (PARROT, PARROT),
        (FISH, FISH),
        (OTHER, OTHER),
    )

    name = models.CharField(
        max_length=30,
    )

    type = models.CharField(
        max_length=max([len(x) for (_, x) in CHOICES]),
        choices=CHOICES,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
        validators=(
            validate_min_year,
            validate_max_year,
        ),
    )

    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,

    )

    @property
    def age(self):
        if self.date_of_birth:
            return datetime.datetime.now().year - self.date_of_birth.year
        return None

    def __str__(self):
        return f"{self.name}"

    class Meta:
        unique_together = ('name', 'owner')
