from django.contrib import admin
from django.urls import path, include  # necesario para incluir rutas de tu app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # aquí conecta las rutas de la app blog
]
