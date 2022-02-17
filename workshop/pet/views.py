from django.db import IntegrityError
from django.shortcuts import render, redirect

from workshop.helpers.is_logged_in import is_logged_in
from workshop.main.views import unauthorized
from workshop.pet.forms import CreatePet, EditPet, DeletePet
from workshop.pet.models import Pet


def pet_actions(request, form_class, success_url, instance, template):
    try:
        if request.method == "POST":
            form = form_class(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return redirect(success_url)
        else:
            form = form_class(instance=instance)
        context = {
            'form': form,
            'pet': instance,
        }
        return render(request, template, context)
    except IntegrityError:
        return redirect('home')


def create_pet(request):
    user = is_logged_in()
    if not user:
        return unauthorized(request)
    return pet_actions(request, CreatePet, 'profile_details', Pet(owner=user), 'pet_create.html')


def edit_pet(request, pk):
    user = is_logged_in()
    pet = Pet.objects.get(pk=pk)
    if not user:
        return unauthorized(request)
    return pet_actions(request, EditPet, 'profile_details', pet, 'pet_edit.html')


def delete_pet(request, pk):
    user = is_logged_in()
    if not user:
        return unauthorized(request)
    pet = Pet.objects.get(pk=pk)
    return pet_actions(request, DeletePet, 'profile_details', pet, 'pet_delete.html')
