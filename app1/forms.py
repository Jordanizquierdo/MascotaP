from django import forms
from app1.models import MascotaM


class FormMascota(forms.ModelForm):
    class Meta(forms.ModelForm):
        model = MascotaM
        fields = '__all__'
