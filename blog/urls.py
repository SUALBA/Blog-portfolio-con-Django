from django.urls import path
from .views import PostListView, SobreMiView, LadoCoderView

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='lista_posts'),
    path('sobre-mi/', SobreMiView.as_view(), name='sobre_mi'),
    path('codigo-de-vida/', LadoCoderView.as_view(), name='lado_coder'),
]