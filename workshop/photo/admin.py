from django.contrib import admin
from workshop.photo.models import Photo


@admin.register(Photo)
class RegisterPhoto(admin.ModelAdmin):
    pass
