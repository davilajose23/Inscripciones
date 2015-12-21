from django.contrib import admin

# Register your models here.
from .models import Proyecto,Usuario

from django.contrib.auth.models import User
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group



admin.site.unregister(Group)

class ProyectoAdmin(admin.ModelAdmin):
    # ...
    list_display = ('nombre', 'codigo', 'descripcion','lugar','horario')
    list_filter = ['pub_date','lugar','horario']
    search_fields = ['nombre','codigo','lugar']

admin.site.register(Proyecto,ProyectoAdmin)
admin.site.register(Usuario)

