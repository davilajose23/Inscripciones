import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# Create your models here.


class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.AutoField(primary_key=True)
    cupo = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=datetime.datetime.now())
    lugar =  models.CharField(max_length=200,null=True)
    horario =  models.CharField(max_length=200,null=True)
    categoria = models.CharField(max_length=50,default='categoria1')
    url = models.CharField(max_length=700,null=True,default='https://pbs.twimg.com/profile_images/498915134073352192/ifsTXFsP.png')
    

    def __str__(self):              # __unicode__ on Python 2
        return self.nombre

    def Proyecto(self):
    	self.lugares_disponibles = self.cupo
  

class Usuario(models.Model):
	user = models.OneToOneField(User)
	first_name = models.CharField(max_length=50,null=True)
	last_name = models.CharField(max_length=50,null=True)
	password = models.CharField(max_length=50,null=True)
	email = models.EmailField(max_length=254,default='example@example.com')
	matricula = models.AutoField(primary_key=True)
	edad = models.IntegerField(null=True)
	added = models.DateTimeField(("Date"), default=datetime.datetime.now())
	direccion = models.CharField(max_length=200,null=True)
	telefono = models.IntegerField(null=True)
	escuela = models.CharField(max_length=50,null=True)
	is_prof = models.BooleanField(default=False)
	nombre_padre = models.CharField(max_length=50,null=True)
	def __str__(self):
		return self.first_name+' '+self.last_name

	

class UsuarioProyecto(models.Model):
	usuario = models.ForeignKey(Usuario)
	proyecto = models.ForeignKey(Proyecto)
	date = models.DateTimeField(("Date"), default=datetime.datetime.now())




