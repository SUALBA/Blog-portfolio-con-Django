# crear_posts.py
import os, django, random
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from blog.models import Post

TITULOS = [
    "¡Bienvenidos al blog!",
    "Mi primer tutorial de Django",
    "Cómo usar React con Django",
    "5 tips de ciberseguridad",
    "Automatizando tareas con Python",
    "Diseño responsive en CSS",
    "Introducción a Docker",
    "Potencia tu workflow en la terminal",
    "IA y ChatGPT: primeros pasos",
    "Excel avanzado para desarrolladores",
]

for i in range(1, 21):
    post = Post(
        titulo=random.choice(TITULOS) + f" (#{i})",
        contenido="Lorem ipsum dolor sit amet, consectetur adipisicing elit…",
        fecha_publicacion=timezone.now(),
        categoria=random.choice([c[0] for c in Post._meta.get_field('categoria').choices])
    )
    post.save()
    print(f"✅ Post creado: {post.titulo}")
