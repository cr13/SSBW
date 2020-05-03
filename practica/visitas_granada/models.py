# -*- coding: utf-8 -*-
from django.db import models

from sorl.thumbnail import ImageField
from django.template.defaultfilters import slugify
import os
from django.core.exceptions import ValidationError

def validate_capitalized(value):
	if value != value.capitalize():
		raise ValidationError('La primera letra de la descripción debe ser mayuscula! Ej: %(value)s',
							  code='invalid',
							  params={'value': value.capitalize()})

# Create your models here.
# visitas_granada/model.py

class Visita(models.Model):
	nombre = models.CharField(max_length=100)
	foto= ImageField(upload_to='fotos', blank=True)
	#foto = models.FileField(upload_to='fotos', blank=True)
	descripcion = models.CharField(max_length=1000, validators=[validate_capitalized])
	likes = models.IntegerField(default=0)
	slug = models.SlugField(unique=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.nombre)
		super(Visita, self).save(*args, **kwargs)

	def __str__(self):  #For Python 2, use __str__ on Python 3
		return self.nombre

	def borrarVisita(self,visita_id):
		visita_obj = Visita.objects.get(id=visita_id)
		visita_obj.delete()
	
	def modiVisita(self, data, visita_id):

		nombre=data['nombre']
		descripcion= data['descripcion']
		# likes= data['likes']
		foto= data['foto']
		visita_obj = Visita.objects.get(id=visita_id)
		if not foto:
			foto = visita_obj.foto
		visita_obj.nombre = nombre
		visita_obj.descripcion = descripcion
		visita_obj.foto = foto
		visita_obj.save()
		return visita_obj

class Comentario(models.Model):
	visita = models.ForeignKey(Visita, on_delete=models.CASCADE)
	texto = models.CharField(max_length=500)
	slug = models.SlugField()

	def save(self, *args, **kwargs):
		self.slug = slugify(self.texto)
		super(Comentario, self).save(*args, **kwargs)


	def __str__(self):	  #For Python 2, use __str__ on Python 3
		return self.texto