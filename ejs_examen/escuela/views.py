from django.shortcuts import render
from .models import Alumno
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def imp_alumn(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        DNI = data.get('DNI')
        nombre = data.get('Nombre')
        try:
            Alumno.objects.create(DNI=DNI, nombre=nombre)
            return HttpResponse("Alumno añadido")
        except:
            return HttpResponseBadRequest("Error al añadir alumno.")
    else:
        return HttpResponseBadRequest("Solo se acepta post.")


@csrf_exempt
def show_alumn(request):
    data = Alumno.objects.values('DNI', 'nombre')
    return HttpResponse(data, content_type='application/json')


@csrf_exempt
def del_alumn(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        DNI = data.get('DNI')
        try:
            dele = Alumno.objects.filter(DNI=DNI).delete()
            return HttpResponse("Alumno borrado de la db.")
        except Exception:
            return HttpResponseBadRequest("Fallo al borrar alumno")
    else:
        return HttpResponseBadRequest("Fallo")

