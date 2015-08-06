from django import forms
from .models import Paciente, Medico, Especialidade
from django.db import connection

"""def get_especialidade():
    especialidade = connection.cursor()
    especialidade.execute("select especialidade_nome, especialidade_nome from hospital_especialidade")
    return especialidade.fetchall()

def get_medico():
    medico = connection.cursor()
    medico.execute("select medico_nome, medico_nome from hospital_medico")
    return medico.fetchall()"""


class PacienteForm(forms.Form):
#This fields must be match with views fields
	nome = forms.CharField()
	data_nascimento = forms.DateField(required=True)
	sexo = forms.CharField(required=True)
	naturalidade = forms.CharField(required=True)
	estado_civil = forms.CharField(required=True)
	numero_bi = forms.CharField(required =True)
	data_de_emissao_bi = forms.DateField(required=True)
	data_de_validade = forms.DateField(required=True)
	data_da_consulta = forms.DateField(required=True)
	especialidade = forms.CharField(required=True)
	medico = forms.CharField(required=True)



class PesquisaForm(forms.Form):
	especialidade = forms.CharField(required=True)
	medico = forms.CharField(required=True)
	data = forms.DateField(required=True)
	nome = forms.CharField(required=True)
	


