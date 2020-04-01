from django import forms
from visitas_granada.models import Visita, Comentario
# from django.contrib.auth.models import User

class VisitaForm(forms.ModelForm):
	# nombre = forms.CharField(max_length=128, help_text="Visita")
	# descripcion = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'cols': 50}),max_length=200, help_text="Introduce la descripción de la visita")
	# foto = forms.FileInput()
	# slug = forms.CharField(widget=forms.HiddenInput(), required=False)

	class Meta:
		model = Visita
		fields = ['nombre', 'descripcion', 'foto']
		widgets = {
			'nombre': forms.TextInput(attrs={'label':'Nombre', 'size': 40}),
			'descripcion': forms.Textarea(attrs={'rows': 3, 'cols': 50}),
			'foto': forms.FileInput()
		}

		def ModificarVisita(self):
			cargaVisita=Visita()
			console.log("---------ModificarVisita-----------Forms---")
			return cargaVisita.modiVisita(self.cleaned_data)
