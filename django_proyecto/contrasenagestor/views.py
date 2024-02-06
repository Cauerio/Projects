from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .models import Datos
from django.views.decorators.csrf import csrf_exempt


def index(request):
    print("Hello")
    return HttpResponse("Hello from index view")

@csrf_exempt
def create_pass(request):
    # Recupera los datos de la URL
    usuario = request.GET.get('usuario', '')
    password = request.GET.get('password', '')

    # Crea una nueva instancia de Datos y guarda en la base de datos
    Datos.objects.create(usuario=usuario, password=password)
    
    return HttpResponse("Password created successfully")
    
@csrf_exempt
def show_pass(request):
    # Aquí deberías manejar la lógica para mostrar todas las contraseñas
    data = serializers.serialize('json', Datos.objects.all())
    return HttpResponse(data, content_type='application/json')

@csrf_exempt
def del_pass(request, usuario, password):
    # Aquí deberías manejar la lógica para eliminar una contraseña por su ID
    Datos.objects.filter(usuario=usuario, password=password).delete()
    return HttpResponse("Password deleted successfully")

@csrf_exempt
def chang_pass(request, id_usuario):
    # Aquí deberías manejar la lógica para cambiar la contraseña por su ID
    Datos.objects.filter(id_usuario=id_usuario).update(password='nueva_contraseña')
    return HttpResponse("Password changed successfully")