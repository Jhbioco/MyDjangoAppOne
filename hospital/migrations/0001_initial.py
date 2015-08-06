# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('especialidade_nome', models.CharField(max_length=100)),
                ('especialidade_descricao', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('medico_nome', models.CharField(max_length=100)),
                ('medico_nivel_academico', models.CharField(max_length=100, choices=[(b'Licenciado', b''), (b'Especialista', b''), (b'Mestre', b''), (b'Doutorado', b'')])),
                ('medico_funcao', models.CharField(max_length=100, choices=[(b'Diretor Geral', b''), (b'Diretor Clinico', b''), (b'Chefe do Banco de Urg\xc3\xaancia', b''), (b'Administrador', b'')])),
                ('medico_data_nascimento', models.DateField()),
                ('medico_especialidade', models.ForeignKey(to='hospital.Especialidade')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('paciente_nome', models.CharField(max_length=100)),
                ('paciente_naturalidade', models.CharField(max_length=100, choices=[(b'Luanda', b''), (b'Namibe', b''), (b'Cabinda', b''), (b'Moxico', b''), (b'Benguela', b''), (b'Huila', b''), (b'Huambo', b'')])),
                ('paciente_pais', models.CharField(max_length=100, choices=[(b'Angola', b''), (b'Portugal', b''), (b'Brasil', b''), (b'Alemanha', b''), (b'Mo\xc3\xa7ambique', b''), (b'Cabo Verde', b''), (b'Namibia', b'')])),
                ('paciente_data_nascimento', models.DateField()),
                ('paciente_estado_civil', models.CharField(max_length=100, choices=[(b'Solteiro(a)', b''), (b'Casado(a)', b''), (b'Divorciado(a)', b''), (b'Viuvo(a)', b'')])),
                ('paciente_bilhete_identidade', models.CharField(max_length=50)),
                ('paciente_bi_emissao', models.DateField()),
                ('paciente_bi_validade', models.DateField()),
                ('paciente_data_consulta', models.DateField()),
                ('paciente_especialidade', models.ForeignKey(to='hospital.Especialidade')),
                ('paciente_medico', models.ForeignKey(to='hospital.Medico')),
            ],
        ),
    ]
