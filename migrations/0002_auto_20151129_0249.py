# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('inscripciones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='direccion',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='escuela',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='nombre_padre',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='telefono',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='pub_date',
            field=models.DateTimeField(default=datetime.date.today, verbose_name=b'date published'),
        ),
    ]
