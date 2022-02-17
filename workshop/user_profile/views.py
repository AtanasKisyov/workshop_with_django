from django.shortcuts import render, redirect

from workshop.main.views import is_logged_in, unauthorized
from workshop.pet.models import Pet
from workshop.photo.models import Photo
from workshop.user_profile.forms import CreateProfile, EditProfile, DeleteProfile
from workshop.user_profile.models import Profile


def profile_action(request, form_class, success_url, instance, template):
    if request.method == 'POST':
        form = form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = form_class(instance=instance)
    context = {
        'form': form,
    }
    return render(request, template, context)


def profile_details(request):
    user = is_logged_in()
    if not user:
        return unauthorized(request)
    user_photos = Photo.objects.filter(tagged_pets__owner=user).distinct()
    pictures_count = user_photos.count()
    pets = Pet.objects.filter(owner=user)
    likes = sum([p.likes for p in user_photos])
    context = {
        'user': user,
        'pictures_count': pictures_count,
        'likes': likes,
        'pets': pets,
    }
    return render(request, 'profile_details.html', context)


def profile_create(request):
    return profile_action(request, CreateProfile, 'home', Profile(), 'profile_create.html')


def profile_edit(request):
    user = is_logged_in()
    if not user:
        return unauthorized(request)
    return profile_action(request, EditProfile, 'profile_details', user, 'profile_edit.html')


def profile_delete(request):
    user = is_logged_in()
    if not user:
        return unauthorized(request)
    return profile_action(request, DeleteProfile, 'home', user, 'profile_delete.html')
