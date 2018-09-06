from django import forms
from uploads.core.models import Document

class ImageForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('image', )
