from django import forms
from .models import Marca, Auto, Cliente

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'


class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = '__all__'


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        

class BuscarAutoForm(forms.Form):
    modelo = forms.CharField(max_length=50, required=False)
    


