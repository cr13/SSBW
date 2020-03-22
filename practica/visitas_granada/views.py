from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from visitas_granada.models import Visita, Comentario

# Create your views here.

def index(request):
    listado_visitas = Visita.objects.order_by('-likes')[:6]
    template = loader.get_template('visitas_granada/index.html')
    context = {
        'listado_visitas': listado_visitas,
    }
    return HttpResponse(template.render(context, request))



def detalle_visita(request, visita_id):
    listado_visitas = Visita.objects.order_by('-likes')[:6]
    visita = get_object_or_404(Visita, pk=visita_id)
    return render(request, 'visitas_granada/detalle_visita.html', {'visita': visita, 'listado_visitas': listado_visitas})

def get_visita(request, visita_name_slug):

    template = loader.get_template('visitas_granada/detalle_visita.html')

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:
        listado_visitas = Visita.objects.all()
        context_dict['visitas']= listado_visitas
        visita = Visita.objects.get(slug=visita_name_slug)
        
        # comentarios = Comentario.objects.all()
        # context_dict['comentarios']= comentarios

        # comentario = Comentario.objects.get(slug=visita_comentario_slug, visita=visita)
        # context_dict['comentario_id'] = comentario
        # context_dict['visita'] = comentario.visita
        # context_dict['texto'] = comentario.texto
     
        # # Adds our results list to the template context under name pages.
        # context_dict['comentarios'] = comentarios
    except visita.DoesNotExist:
        pass

    # Go render the response and return it to the client.
    return HttpResponse(template.render(context, request))

    # return render(request, 'app/detalle_visita.html', context_dict)