from django import forms
from .models import Reserva

class Reserva_Formulario(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'
