# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_auto_20150729_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='paciente_sexo',
            field=models.CharField(default=b'masculino', max_length=20),
        ),
    ]
