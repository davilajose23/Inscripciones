# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('nombre', models.CharField(max_length=100)),
                ('codigo', models.AutoField(serialize=False, primary_key=True)),
                ('cupo', models.IntegerField()),
                ('descripcion', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('lugar', models.CharField(max_length=200, null=True)),
                ('horario', models.CharField(max_length=200, null=True)),
                ('categoria', models.CharField(default=b'categoria1', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('password', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(default=b'example@example.com', max_length=254)),
                ('matricula', models.AutoField(serialize=False, primary_key=True)),
                ('edad', models.IntegerField(null=True)),
                ('added', models.DateField(default=datetime.date.today, verbose_name=b'Date')),
                ('is_prof', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioProyecto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(default=datetime.date.today, verbose_name=b'Date')),
                ('proyecto', models.ForeignKey(to='inscripciones.Proyecto')),
                ('usuario', models.ForeignKey(to='inscripciones.Usuario')),
            ],
        ),
    ]
