from django import forms

from workshop.pet.models import Pet
from workshop.photo.models import Photo
from workshop.user_profile.models import Profile


class CreateProfile(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'picture')
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter first name',
                    'class': 'form-control',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter last name',
                    'class': 'form-control',
                }
            ),
            'picture': forms.TextInput(
                attrs={
                    'placeholder': 'Enter URL',
                    'class': 'form-control',
                }
            )
        }


class EditProfile(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial['gender'] = Profile.DO_NOT_SHOW

    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'picture': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Enter your email',
                    'class': 'form-control',
                }
            ),
            'gender': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'rows': 3,
                    'placeholder': 'Enter description',
                    'class': 'form-control',
                }
            ),
        }


class DeleteProfile(forms.ModelForm):

    def save(self, commit=True):
        pets = list(self.instance.pet_set.all())
        Photo.objects.filter(tagged_pets__in=pets).delete()
        self.instance.delete()

    class Meta:
        model = Profile
        fields = ()
