# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscripciones', '0002_auto_20151129_0249'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='url',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
