from django.urls import path
from . import views

urlpatterns = [
    path('import/', views.imp_books, name='imp_books'),
    path('show/', views.show_books, name='show_books'),
    path('delete/', views.del_book, name='del_book')
]