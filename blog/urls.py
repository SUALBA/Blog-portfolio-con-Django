from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_posts, name='lista_posts'),
    path('sobre-mi/', views.sobre_mi, name='sobre_mi'),
    path('codigo-de-vida/', views.lado_coder, name='lado_coder'),
]

