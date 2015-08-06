#!/usr/bin/python
# -*- coding: latin-1 -*-
from django.db import models
from datetime import datetime
from django.db import connection

# Create your models here.

class Especialidade(models.Model):
	especialidade_nome = models.CharField(max_length=100, blank=False)
	especialidade_descricao = models.CharField(max_length=300)

	def __str__(self):
		return self.especialidade_nome

class Medico(models.Model):
	medico_nome = models.CharField(max_length=100)
	medico_especialidade = models.ForeignKey(Especialidade)
	medico_nivel_academico = models.CharField(max_length=100)
	medico_funcao = models.CharField(max_length=100)
	medico_data_nascimento = models.DateField()

	def __str__(self):
		return self.medico_nome


class Paciente(models.Model):
	paciente_nome = models.CharField(max_length=100)
	paciente_sexo= models.CharField(max_length=20, default='masculino')
	paciente_naturalidade = models.CharField(max_length=100)
	paciente_pais = models.CharField(max_length=100)
	paciente_data_nascimento = models.DateField()
	paciente_estado_civil = models.CharField(max_length=100)
	paciente_bilhete_identidade = models.CharField(max_length=50)
	paciente_bi_emissao = models.DateField()
	paciente_bi_validade = models.DateField()
	paciente_data_consulta = models.DateField()
	paciente_especialidade = models.ForeignKey(Especialidade)
	paciente_medico = models.ForeignKey(Medico)
	def __str__(self):
		return self.paciente_nome

