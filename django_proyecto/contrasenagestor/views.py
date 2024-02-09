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
        usuario = data.get('usuario')
        password = data.get('password')

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
            dele = Datos.objects.filter(id_usuario=id_usuario).delete()
            return HttpResponse("Usuario borrado.")
        except Exception:
            return HttpResponseBadRequest("Fallo al borrar el usuario")
    else:
        return HttpResponseBadRequest("Fallo")




@csrf_exempt
def chang_pass(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        id_usuario = data.get('id_usuario')
        usuario = data.get('usuario')
        password = data.get('password')
        try:
            Datos.objects.filter(id_usuario=id_usuario).update(usuario=usuario ,password=password)
            return HttpResponse("La password y el usuario ha cambiado")
        except Exception:
            return HttpResponseBadRequest("Fallo al cambiar el usuario")
    else:
        return HttpResponseBadRequest("Fallo")
    

@csrf_exempt
def show_users(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        usuario = data.get('usuario')
        try:
            posts = Datos.objects.filter(usuario=usuario).count()
            return JsonResponse({'count':posts})
        except Exception:
            return HttpResponse("Fallo al encontrar usuario")
    else:
        return HttpResponse("Fallo")
    
# Hacer un contador de usuarios eliminados de la base de datos.
# Contar las ids inexistentes con el limite de la ultima id creada.
"""    
@csrf_exempt
def count_id_del(request): 
    
    data = serializers.serialize('json', Datos.objects.all())
    delet = Datos.objects.filter(id_usuario__isnull=True)
    d = serializers.serialize('json', Datos.objects.filter(id_usuario__isnull=False).distinct())
    d.count('id_usuario')
    return JsonResponse({'count':d})
    
    """



@csrf_exempt
def mi_vista_sin_proteccion_csrf(request):
    return JsonResponse("Esta vista no tiene protección CSRF.")