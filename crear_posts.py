# crear_posts.py
import os
import django
import random
from datetime import datetime, timedelta

# Preparar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from blog.models import Post

# Lista de títulos de ejemplo
titulos = [
    "Proyecto Web Avanzado",
    "Curso de Ciberseguridad",
    "Diseño con React",
    "Backend con Django",
    "Introducción a la Terminal",
    "Contenedores con Docker",
    "Automatización con Python",
    "Excel para Analistas",
    "Portfolio Frontend Vue.js",
    "Optimización SEO en 2025",
    "Primeros pasos en Salesforce",
    "APIs REST con Django",
    "Git y Github Pro",
    "Full Stack Developer Life",
    "Scrum para Proyectos IT",
    "UI/UX Moderno",
    "Startups: cómo lanzar tu idea",
    "Cybersecurity Bootcamp",
    "Programación Limpia en Python",
    "Técnicas de Debugging en VSCode"
]

# Limpieza previa opcional
# Post.objects.all().delete()

for titulo in titulos:
    contenido = f"Contenido de ejemplo para el post: {titulo}. Este artículo habla de {titulo.lower()} y su impacto en el desarrollo moderno."
    fecha = datetime.now() - timedelta(days=random.randint(1, 300))
    
    post = Post(
        titulo=titulo,
        contenido=contenido,
        fecha_publicacion=fecha
    )
    post.save()

print("✅ 20 posts creados exitosamente.")
