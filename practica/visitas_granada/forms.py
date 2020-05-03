from django import forms
from django.contrib.admin.widgets import AdminFileWidget
from visitas_granada.models import Visita, Comentario
from sorl.thumbnail import get_thumbnail
import os


# class AdminImageWidget(AdminFileWidget):
#   def render(self, name, value, attrs=None):
#     output = []
#     if value and getattr(value, "url", None):
#       t = get_thumbnail(value,'80x80')
#       output.append('<img src="{}">'.format(t.url))
#     output.append(super(AdminFileWidget, self).render(name, value, attrs))
#     return mark_safe(u''.join(output))

class VisitaForm(forms.ModelForm):

	class Meta:
		model = Visita
		fields = ['nombre', 'descripcion', 'foto']
		widgets = {
			'nombre': forms.TextInput(attrs={'label':'Nombre', 'size': 40}),
			'descripcion': forms.Textarea(attrs={'rows': 3, 'cols': 50}),
			# 'foto':  AdminImageWidget, Error al renderizar con  crispy_field
		}

	def ModificarVisita(self, visita_id):
		cargaVisita=Visita()
		return cargaVisita.modiVisita(self.cleaned_data, visita_id)

