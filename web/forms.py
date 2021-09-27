from django import forms
from .models import note


class Formaddnote(forms.ModelForm):
    class Meta:
        model = note
        fields = '__all__'
