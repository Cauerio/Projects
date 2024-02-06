from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_pass, name='create_pass'),
    path('show/', views.show_pass, name='show_pass'),
    path('change/<int:id_usuario>/', views.chang_pass, name='change_pass'),
    path('delete/<int:id_usuario>/', views.del_pass, name='delete_pass'),
]
