from django import forms
from .models import HandwritingAnalysis

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = HandwritingAnalysis
        fields = ['user','handwriting_image']