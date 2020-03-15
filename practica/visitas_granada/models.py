# -*- coding: utf-8 -*-
from django.db import models

from sorl.thumbnail import ImageField
from django.template.defaultfilters import slugify
import os

# Create your models here.
# visitas_granada/model.py

class Visita(models.Model):
	nombre = models.CharField(max_length=100)
	foto= ImageField(upload_to='fotos')
	#foto = models.FileField(upload_to='fotos', blank=True)
	descripcion = models.CharField(max_length=1000)
	likes = models.IntegerField(default=0)
	slug = models.SlugField(unique=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.nombre)
		super(Visita, self).save(*args, **kwargs)

	def __str__(self):  #For Python 2, use __str__ on Python 3
		return self.nombre

class Comentario(models.Model):
	visita = models.ForeignKey(Visita, on_delete=models.CASCADE)
	texto = models.CharField(max_length=500)
	slug = models.SlugField()

	def save(self, *args, **kwargs):
		self.slug = slugify(self.texto)
		super(Comentario, self).save(*args, **kwargs)


	def __str__(self):	  #For Python 2, use __str__ on Python 3
		return self.texto