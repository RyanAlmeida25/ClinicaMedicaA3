from django import forms
from .models import *


class medicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ["nome", "especialidade"]

class especialidadeForm(forms.ModelForm):
    class Meta:
        model = Especialidade
        fields = ["nome"]


class pacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ["nome", "data_nascimento"]

class consultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ["medico", "paciente", "data_hora"]



