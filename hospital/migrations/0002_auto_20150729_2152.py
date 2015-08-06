# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='medico_funcao',
            field=models.CharField(max_length=100, choices=[(b'Diretor Geral', b'Diretor Geral'), (b'Diretor Clinico', b'Diretor Clinico'), (b'Chefe do Banco de Urg\xc3\xaancia', b'Chefe do Banco de Urg\xc3\xaancia'), (b'Administrador', b'Administrador')]),
        ),
        migrations.AlterField(
            model_name='medico',
            name='medico_nivel_academico',
            field=models.CharField(max_length=100, choices=[(b'Licenciado', b'Licenciado'), (b'Especialista', b'Especialista'), (b'Mestre', b'Mestre'), (b'Doutorado', b'Doutorado')]),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='paciente_estado_civil',
            field=models.CharField(max_length=100, choices=[(b'Solteiro(a)', b'Solteiro(a)'), (b'Casado(a)', b'Casado(a)'), (b'Divorciado(a)', b'Divorciado(a)'), (b'Viuvo(a)', b'Viuvo(a)')]),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='paciente_naturalidade',
            field=models.CharField(max_length=100, choices=[(b'Luanda', b'Luanda'), (b'Namibe', b'Namibe'), (b'Cabinda', b'Cabinda'), (b'Moxico', b'Moxico'), (b'Benguela', b'Benguela'), (b'Huila', b'Huila'), (b'Huambo', b'Huambo')]),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='paciente_pais',
            field=models.CharField(max_length=100, choices=[(b'Angola', b'Angola'), (b'Portugal', b'Portugal'), (b'Brasil', b'Brasil'), (b'Alemanha', b'Alemanha'), (b'Mo\xc3\xa7ambique', b'Mo\xc3\xa7ambique'), (b'Cabo Verde', b'Cabo Verde'), (b'Namibia', b'Namibia')]),
        ),
    ]
