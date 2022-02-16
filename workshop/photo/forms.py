from django import forms

from workshop.photo.models import Photo


class CreatePhoto(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ('photo', 'description', 'tagged_pets')
        widgets = {
            'description': forms.Textarea(
                attrs={
                    'rows': 3,
                    'placeholder': 'Enter description',
                    'class': 'form-control',
                }
            ),
            'tagged_pets': forms.SelectMultiple(
                attrs={
                    'class': 'form-control',
                }
            )
        }


class EditPhoto(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ('description', 'tagged_pets')
        widgets = {
            'description': forms.Textarea(
                attrs={
                    'rows': 3,
                    'placeholder': 'Enter description',
                    'class': 'form-control',
                }
            ),
            'tagged_pets': forms.SelectMultiple(
                attrs={
                    'class': 'form-control',
                }
            )
        }


class DeletePhoto(forms.ModelForm):

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Photo
        fields = ()
