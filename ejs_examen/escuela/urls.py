from . import views
from django.urls import path

urlpatterns = [
    path('import/', views.imp_alumn, name='imp_alumn'),
    path('show/', views.show_alumn, name='show_alumn'),
    path('delete/', views.del_alumn, name='del_alumn')
]