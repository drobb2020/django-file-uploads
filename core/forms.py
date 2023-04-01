from django import forms

from core.models import Dog


class DogForm(forms.ModelForm):
    """Form for adding a dog and image to the database."""
    class Meta:
        model = Dog
        fields = ('name', 'image',)
        widgets = {
            'image': forms.FileInput(attrs={'accept': '.png, .jpg, .pdf'})
        }
