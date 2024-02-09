from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_pass, name='create_pass'),
    path('show/', views.show_pass, name='show_pass'),
    path('change/', views.chang_pass, name='change_pass'),
    path('delete/', views.del_pass, name='delete_pass'),
    path('showuser/', views.show_users, name='show_users'),
    path('count_ids_del/', views.count_id_del, name='count_id_del')
]
