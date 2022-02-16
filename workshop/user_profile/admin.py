from django.contrib import admin

from workshop.user_profile.models import Profile


@admin.register(Profile)
class RegisterUser(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'picture',
    )
