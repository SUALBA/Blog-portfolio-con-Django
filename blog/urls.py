from django.urls import path
from .views import PostListView, SobreMiView, LadoCoderView
from .views import DetallePostView
from . import views

app_name = 'blog'

urlpatterns = [
    # Home (página de inicio)
    path('', views.home_view, name='home'),
    
    # Blog (lista de posts) - ¡OJO: 'lista_posts' en plural!
    path('blog/', PostListView.as_view(), name='lista_posts'),
    
    # Otras rutas
    path('sobre-mi/', SobreMiView.as_view(), name='sobre_mi'),
    path('codigo-de-vida/', LadoCoderView.as_view(), name='lado_coder'),
    path('post/<slug:slug>/', DetallePostView.as_view(), name='detalle_post'),
    path('post/<int:pk>/signal/', views.signal_post, name='signal_post'),
    path('contacto/', views.contacto_view, name='contacto'),
     path('proyectos/', views.proyectos, name='proyectos'),
]



