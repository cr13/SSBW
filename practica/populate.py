# -*- coding: utf-8 -*-
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','mi_sitio_web.settings')

import django
django.setup()

from visitas_granada.models import Visita, Comentario


def populate():
	visita1= add_visita(nombre='Recogidas', descripcion='Ir de tiendas', like=1)

	add_comentario(visita=visita1, texto="Kiko Milano 25 porceiento descuento en toda la tienda ")

	add_comentario(visita=visita1, texto="Burger king dia sin IVA")

	add_comentario(visita=visita1, texto="Espectaculos por dia Andalucia")

	visita2= add_visita(nombre='Parque de las ciencias',descripcion='Impresionante multitud de secciones',like= 1)

	add_comentario(visita=visita2, texto="Subir a la torre")

	add_comentario(visita=visita2, texto="Mariposario espectacular")

	add_comentario(visita=visita2, texto="Biodomo, jaleo de animales")


def add_visita(nombre, descripcion, like):
	v = Visita.objects.get_or_create(nombre=nombre)[0]
	v.descripcion=descripcion
	v.likes=like
	v.save()
	return v

def add_comentario(visita, texto):
	com_v = Comentario.objects.get_or_create(visita=visita)[0]
	com_v.texto=texto
	com_v.save()
	return com_v
	
if __name__ == "__main__":
		
	#v = Visita(nombre="PTS", descripcion="CPD Hospital PTS")
	#v.save()

	# = Comentario(v[0], "Vistas maravillosas")
	#c.save()

	#c = Comentario(v[0], "Gran prevision de futuro de cara al BIG DATA")
	#c.save()

	populate()

	print(Visita.objects.all())