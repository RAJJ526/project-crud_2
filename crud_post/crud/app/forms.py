from django import forms
from .models import *

class MobileForm(forms.ModelForm):
    class Meta:
        model=Employes
        fields="__all__"



