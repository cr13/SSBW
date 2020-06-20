from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.template import loader
from visitas_granada.models import Visita, Comentario
from visitas_granada.forms import VisitaForm
import json
from django.core import serializers
from django.forms.models import model_to_dict
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, permissions
from rest_framework.parsers import JSONParser
from visitas_granada.serializers import VisitaSerializer, ComentarioSerializer, GestionLikesSerializer
import requests
import datetime
from decouple import config

import logging
logger = logging.getLogger(__name__)


# Create your views here.

def index(request):
    listado_visitas = Visita.objects.order_by('-likes')[:6]
    numero_visitas = Visita.objects.all().count()
    template = loader.get_template('visitas_granada/index.html')
    context = {
        'listado_visitas': listado_visitas,
        'numero_visitas': numero_visitas,
    }
    return HttpResponse(template.render(context, request))



def detalle_visita(request, visita_id):
    listado_visitas = Visita.objects.order_by('-likes')[:10]
    comentarios = Comentario.objects.all()
    visita = get_object_or_404(Visita, pk=visita_id)
    form_visita = VisitaForm(instance=visita)    
    lugar_buscar = visita.nombre.replace(" ", "+") + "+Granada"
    # logger.warning(lugar_buscar)
    ubi = 'https://nominatim.openstreetmap.org/search?q={}&format=json'.format(lugar_buscar)
    result = requests.get(ubi)
    # logger.warning(result.text)
    data = json.loads(result.text)
    if data:     
        lat = data[0]['lat']
        lon = data[0]['lon']
    else:
        logger.warning("Visita no ubicada, ubicamos la visita en Granada")        
        lat = '37.183054'
        lon = '-3.6021928'

    return render(request, 'visitas_granada/detalle_visita.html', {'visita': visita, 'listado_visitas': listado_visitas, 'form_visita':form_visita, 'comentarios': comentarios, 'lat': lat, 'lon': lon})

@login_required
@staff_member_required
@permission_required('polls.add_choice', raise_exception=True)
def add_visita(request):

    if request.method == 'POST':   # de vuelta con los datos

        form = VisitaForm(request.POST, request.FILES) #  bound the form

        if form.is_valid():
            form.save()
            notify_bot("Nueva visita disponible")
            return redirect('index')
            
        context = {
            'form_visita': form
        }
    # GET o error
    else:
        # If the request was not a POST, display the form to enter details.
        form = VisitaForm()

    context = {}
    context['form_visita'] = form

    return render(request, "visitas_granada/add_visita.html", context)

@login_required
@staff_member_required
@permission_required('polls.add_choice', raise_exception=True)
def edit_visita(request, visita_id):
    # if this is a POST request we need to process the form data

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = VisitaForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # nombre = form.cleaned_data['nombre']
            # desc = form.cleaned_data['descripcion']
            # foto = form.cleaned_data['foto']
            # print(nombre)
            # # listado_visitas = Visita.objects.order_by('-likes')[:6]
            # visita = get_object_or_404(Visita, pk=visita_id)
            # # visita = Visita.get_object(pk=visita_id)
            # visita.nombre = nombre
            # visita.descripcion = desc
            # visita.foto = foto
            # visita.save()
            # print(visita)
            result = form.ModificarVisita(visita_id)
            dict_obj = model_to_dict(result )
            # print(dict_obj)
            if 'foto' in dict_obj:
                logger.warning("Se elimina el campo foto por formato indebido")
                del dict_obj['foto']
            return JsonResponse({'mensaje':dict_obj}) 

        else:
            return JsonResponse({'mensaje':form.errors},status=500)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = VisitaForm()
        # visita = Visita.objects.get(pk=visita_id)
        # form = VisitaForm(instance=visita)
    # return render(request, "visitas_granada/edit_visita.html", context)
    return JsonResponse({"error": ""}, status=400)

@login_required
@staff_member_required
@permission_required('polls.add_choice', raise_exception=True)
def del_visita(request, visita_id):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        return JsonResponse({'mensaje':'Estas usando POST'})

    # if a GET (or any other method) we'll create a blank form
    else:
        vistitas=Visita()
        vistitas.borrarVisita(visita_id)
        logger.info("Visita con id %s  ha sido eliminada", visita_id)

    return redirect('index')
    # return JsonResponse({'mensaje':True})

class VisitaViewSet(viewsets.ModelViewSet):
    serializer_class = VisitaSerializer
    queryset = Visita.objects.all().order_by('nombre')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  

class ComentarioViewSet(viewsets.ModelViewSet):
    serializer_class = ComentarioSerializer    
    queryset = Comentario.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

@csrf_exempt
def likes_gestion(request, visita_id):
    try:
        visita = Visita.objects.get(id=visita_id)
    except Visita.DoesNotExist:
        logger.exception("Error visita "+ visita_id + " no encontrada" )
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = GestionLikesSerializer(visita)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = GestionLikesSerializer(visita, data=data)
        if serializer.is_valid():
            serializer.save()
            notify_bot("Actualización de likes en visita "+ visita.nombre)
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

def notify_bot(notify):

    token = config('TELEGRAM_TOKEN')
    chat_id = config('TELEGRAM_CHAT_ID')

    dt = datetime.datetime.utcnow().strftime('%d-%m-%Y %H:%M:%S')   
    msg = "<i>{datetime}</i><pre>\n{notify}</pre>".format(notify=notify, datetime=dt)
    
    logger.info("Notifcación a bot telegram "+ msg)
    
    if token != "None" and chat_id != "None":
        payload = {
            'chat_id': chat_id,
            'text': msg,
            'parse_mode': 'HTML'
        }
        result = requests.post("https://api.telegram.org/bot{token}/sendMessage".format(
            token=token),
            data=payload).content

        # print(result)