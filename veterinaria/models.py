from django.db import models

# Create your models here.
class Mascotas(models.Model):
  nombre=models.CharField(max_length=30, help_text='Nombre de su mascota')
  raza=models.CharField(max_length=25, help_text='Raza de su mascota')
  edad=models.IntegerField(help_text='edad')
  sexo=models.CharField(max_length=30,help_text='sexo de su mascota')

  
class Alimentos(models.Model):
  codigo=models.CharField(max_length=10,help_text='Codigo de alimento')
  tipo_alimento=models.CharField(max_length=20,help_text='Tipo de alimento de mascota')
  marca=models.CharField(max_length=200,help_text='Marca de producto')
  cantidad=models.IntegerField(help_text='Cantidad del producto')
  precio=models.FloatField(help_text='Precio del producto')


class Accesorios(models.Model):
  marca=models.CharField(max_length=200,help_text='Marca')
  nombre=models.CharField(max_length=30,help_text='Nombre')
  codigo=models.FloatField(help_text='Codigo')
  color=models.CharField(max_length=100,help_text='Color')
  tamaño=models.CharField(max_length=100,help_text='tamaño')