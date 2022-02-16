from django.db import models

from workshop.helpers.validators import validate_file_size
from workshop.pet.models import Pet


class Photo(models.Model):

    photo = models.ImageField(
        upload_to='images',
        validators=(
            validate_file_size,
        )
    )

    tagged_pets = models.ManyToManyField(
        Pet,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    created_on = models.DateTimeField(
        auto_now_add=True,
    )

    likes = models.IntegerField(
        default=0,
    )

    def __str__(self):
        return f"{self.created_on}"
