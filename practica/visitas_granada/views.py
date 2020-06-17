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

import logging


# Create your views here.

def index(request):
	listado_visitas = Visita.objects.order_by('-likes')[:6]
	template = loader.get_template('visitas_granada/index.html')
	context = {
		'listado_visitas': listado_visitas,
	}
	return HttpResponse(template.render(context, request))



def detalle_visita(request, visita_id):
	listado_visitas = Visita.objects.order_by('-likes')[:10]
	visita = get_object_or_404(Visita, pk=visita_id)
	form_visita = VisitaForm(instance=visita)
	return render(request, 'visitas_granada/detalle_visita.html', {'visita': visita, 'listado_visitas': listado_visitas, 'form_visita':form_visita})

@login_required
@staff_member_required
@permission_required('polls.add_choice', raise_exception=True)
def add_visita(request):

	if request.method == 'POST':   # de vuelta con los datos

		form = VisitaForm(request.POST, request.FILES) #  bound the form

		if form.is_valid():
			form.save()
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
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = GestionLikesSerializer(visita)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = GestionLikesSerializer(visita, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

