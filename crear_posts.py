import os
import django
import random
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from blog.models import Post

fake = Faker()

titulos = [
    "Proyecto Web Avanzado", "Diseño con React", "Curso de Ciberseguridad", "Aprendiendo Python",
    "Dominando Django", "Tips de Terminal", "Introducción a IA", "Productividad Tech",
    "Cómo usar GitHub como un Pro", "Primeros pasos en Docker", "Marketing para StartUps",
    "El lado Coder: Motivación", "CSS Creativo", "Backend Best Practices", "Frameworks modernos",
    "Bases de Datos Relacionales", "Excel Hacks", "Salesforce para principiantes", "Tendencias en AI", "Mindset de programador"
]

categorias = [
    'html', 'css', 'js', 'react', 'vue', 'angular', 'backend', 'docker',
    'terminal', 'chatgpt', 'ia', 'python', 'cyber', 'startup', 'excel', 'salesforce', 'code'
]

for i in range(50):
    Post.objects.create(
        titulo=random.choice(titulos),
        contenido=fake.paragraph(nb_sentences=20),
        categoria=random.choice(categorias)
    )

print("✅ ¡50 posts de prueba creados exitosamente!")
