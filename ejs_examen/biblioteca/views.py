from django.shortcuts import render
from .models import Libro
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def imp_books(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        nombre_libro = data.get('titulo')
        paginas = data.get('paginas')
        try:
            Libro.objects.create(nombre_libro=nombre_libro, paginas=paginas)
            return HttpResponse("Libro importado")
        except:
            return HttpResponseBadRequest("Error al importar el libro.")
    else:
        return HttpResponseBadRequest("Solo se acepta post.")


@csrf_exempt
def show_books(request):
    data = serializers.serialize('json', Libro.objects.all())
    return HttpResponse(data, content_type='application/json')


@csrf_exempt
def del_book(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        id_libro = data.get('id_libro')
        try:
            dele = Libro.objects.filter(id_libro=id_libro).delete()
            return HttpResponse("Libro borrado.")
        except Exception:
            return HttpResponseBadRequest("Fallo al borrar el libro")
    else:
        return HttpResponseBadRequest("Fallo")

