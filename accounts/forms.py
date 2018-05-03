from django import forms
from .models import Tapahtuma

class TapahtumaForm(forms.ModelForm):
    class Meta:
        model = Tapahtuma
        fields = ['name', 'description', 'date']
