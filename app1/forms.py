from django import forms
from app1.models import MascotaM


class FormMascota(forms.ModelForm):
    class Meta:
        model = MascotaM
        fields = '__all__'
