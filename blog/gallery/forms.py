from django import forms
from .models import GalleryImages

class GalleryImagesForm(forms.ModelForm):
    class Meta:
        model = GalleryImages
        fields = ['title', 'image']