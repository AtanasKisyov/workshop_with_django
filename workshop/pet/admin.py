from django.contrib import admin

from workshop.pet.models import Pet


@admin.register(Pet)
class RegisterPet(admin.ModelAdmin):
    list_display = (
        'name',
        'owner',
    )
