from django import forms
from .models import *


class Cliente_form(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('__all__')