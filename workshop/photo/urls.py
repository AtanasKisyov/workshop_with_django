from django.urls import path

from workshop.photo.views import photo_details, like_photo, create_photo, edit_photo, delete_photo

urlpatterns = [
    path('details/int:<pk>', photo_details, name='photo_details'),
    path('details/like/int:<pk>', like_photo, name='like_photo'),
    path('add/', create_photo, name='create_photo'),
    path('edit/int:<pk>', edit_photo, name='edit_photo'),
    path('delete/int:<pk>', delete_photo, name='delete_photo')
]
