from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.core import serializers
from .models import Datos
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def create_pass(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        usuario = data.get('usuario', '')
        password = data.get('password', '')

        if not usuario or not password:
            return HttpResponseBadRequest("Se necesita 'usuario' y 'password'.")

        try:
            Datos.objects.create(usuario=usuario, password=password)
            return HttpResponse("Usuario creado")
        except:
            return HttpResponseBadRequest("Error al crear la password.")
    else:
        return HttpResponseBadRequest("Solo se acepta post.")
    
    
@csrf_exempt
def show_pass(request):
    data = serializers.serialize('json', Datos.objects.all())
    return HttpResponse(data, content_type='application/json')


    
@csrf_exempt
def del_pass(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        id_usuario = data.get('id_usuario')
        try:
            Datos.objects.filter(id_usuario=id_usuario).delete()
            return HttpResponse("Usuario borrado.")
        except Exception as e:
            return HttpResponseBadRequest(f"Fallo al borrar el usuario {str(e)}")
    else:
        return HttpResponseBadRequest("Fallo")




@csrf_exempt
def chang_pass(request, id_usuario, usuario, password):
    Datos.objects.filter(id_usuario=id_usuario, usuario=usuario, password=password).update(password='nueva_contraseña')
    return HttpResponse("Password cambiado")