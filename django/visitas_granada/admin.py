from django.contrib import admin

# Register your models here.
from visitas_granada.models import Visita, Comentario

class VisitaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('nombre',)}

class ComentarioAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('texto',)}

admin.site.register(Visita, VisitaAdmin)
admin.site.register(Comentario, ComentarioAdmin)