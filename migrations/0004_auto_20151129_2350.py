# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('inscripciones', '0003_proyecto_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 29, 23, 50, 34, 430745), verbose_name=b'date published'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='url',
            field=models.CharField(default=b'https://pbs.twimg.com/profile_images/498915134073352192/ifsTXFsP.png', max_length=700, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='added',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 29, 23, 50, 34, 431826), verbose_name=b'Date'),
        ),
        migrations.AlterField(
            model_name='usuarioproyecto',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 29, 23, 50, 34, 432833), verbose_name=b'Date'),
        ),
    ]
