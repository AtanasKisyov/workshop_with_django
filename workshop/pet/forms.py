from django import forms

from workshop.pet.models import Pet


class PetModelForm(forms.ModelForm):

    @staticmethod
    def normal_fields():
        return {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter pet name',
                    'class': 'form-control',
                }
            ),
            'type': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'verbose_name': 'Day of Birth',
                }
            )
        }

    @staticmethod
    def disabled_fields():
        return {
            'name': forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                    'class': 'form-control',
                }
            ),
            'type': forms.Select(
                attrs={
                    'readonly': 'readonly',
                    'class': 'form-control',
                }
            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'verbose_name': 'Day of Birth',
                    'readonly': 'readonly',
                }
            )
        }

    class Meta:
        model = Pet
        fields = ('name', 'type', 'date_of_birth')


class CreatePet(PetModelForm):

    class Meta:
        model = Pet
        fields = ('name', 'type', 'date_of_birth')
        widgets = PetModelForm.normal_fields()


class EditPet(PetModelForm):

    class Meta:
        model = Pet
        fields = ('name', 'type', 'date_of_birth')
        widgets = PetModelForm.normal_fields()


class DeletePet(PetModelForm):

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Pet
        fields = ('name', 'type', 'date_of_birth')
        widgets = PetModelForm.disabled_fields()
