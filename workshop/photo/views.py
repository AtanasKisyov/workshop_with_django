from django.shortcuts import render, redirect

from workshop.photo.forms import CreatePhoto, EditPhoto, DeletePhoto
from workshop.photo.models import Photo


def photo_details(request, pk):
    photo = Photo.objects.get(pk=pk)
    context = {
        'photo': photo,
    }
    return render(request, 'photo_details.html', context)


def like_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    photo.likes += 1
    photo.save()
    return photo_details(request, pk)


def photo_actions(request, form_class, success_url, instance, template):
    if request.method == 'POST':
        form = form_class(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = form_class(instance=instance)

    context = {
        'form': form,
        'photo': instance,
    }

    return render(request, template, context)


def create_photo(request):
    return photo_actions(request, CreatePhoto, 'dashboard', Photo(), 'photo_create.html')


def edit_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditPhoto(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            return photo_details(request, photo.id)
    else:
        form = EditPhoto(instance=photo)

    context = {
        'form': form,
        'photo': photo,
    }
    return render(request, 'photo_edit.html', context)


def delete_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    photo_form = DeletePhoto(request.POST, request.FILES, instance=photo)
    photo_form.save()
    return redirect('dashboard')
