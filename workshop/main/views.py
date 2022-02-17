from django.shortcuts import render

from workshop.helpers.is_logged_in import is_logged_in
from workshop.photo.models import Photo


def home(request):
    context = {
        'user': is_logged_in(),
    }
    return render(request, 'home_page.html', context)


def dashboard(request):
    user = is_logged_in()
    if not user:
        return unauthorized(request)
    photos = Photo.objects.filter(
        tagged_pets__owner=user,
    ).distinct()
    context = {
        'photos': photos,
    }
    return render(request, 'dashboard.html', context)


def unauthorized(request):
    return render(request, '401_error.html')
