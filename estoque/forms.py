
from django import forms
from .models import Alimento

class AlimentoForm(forms.ModelForm):
    class Meta:
        model = Alimento
        fields = ['nome', 'quantidade', 'validade', 'peso']
        widgets = {
            'validade': forms.DateInput(attrs={'type': 'date'}),
        }
