from django.http import HttpResponse
from django.template import loader
from visitas_granada.models import Visita, Comentario

# Create your views here.

def index(request):
    listado_visitas = Visita.objects.order_by('-likes')[:5]
    template = loader.get_template('visitas_granada/listado.html')
    context = {
        'listado_visitas': listado_visitas,
    }
    return HttpResponse(template.render(context, request))