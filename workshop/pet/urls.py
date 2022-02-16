from django.urls import path

from workshop.pet.views import create_pet, edit_pet, delete_pet

urlpatterns = [
    path('add/', create_pet, name='create_pet'),
    path('edit/int:<pk>', edit_pet, name='edit_pet'),
    path('delete/int:<pk>', delete_pet, name='delete_pet'),
]
