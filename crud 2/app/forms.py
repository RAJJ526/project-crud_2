from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car  # Fixed typo in 'model'
        fields = "__all__"   # Ensure 'fields' is defined within Meta
