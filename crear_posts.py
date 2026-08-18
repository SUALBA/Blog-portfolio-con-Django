import os
import django
import random
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from blog.models import Post

fake = Faker()

titulos = [
    "ISO 27001: guía práctica para su implementación",
    "ENS: Esquema Nacional de Seguridad paso a paso",
    "NIST CSF: cómo alinear tu estrategia de ciberseguridad",
    "Auditoría de sistemas: metodologías y mejores prácticas",
    "Privacidad por diseño y RGPD en la práctica",
    "AuditSym: automatizando el cumplimiento normativo",
    "Python para automatización de tareas de seguridad",
    "Arquitectura web segura con Django y React",
    "Docker y despliegue seguro en la nube",
    "Hardening de redes: protección perimetral",
    "El lado Coder: reflexiones sobre programación y vida",
    "Análisis de riesgos con MAGERIT",
    "Seguridad en APIs REST: buenas prácticas",
    "Gestión de incidentes: plan de respuesta efectivo",
    "Ciberseguridad en entornos cloud",
]

categorias = [
    'iso27001', 'ens', 'nist', 'auditoria', 'privacidad',
    'auditsym', 'python', 'web', 'devops', 'redes', 'code'
]

for i in range(20):  # Reducido de 50 a 20
    Post.objects.create(
        titulo=random.choice(titulos),
        contenido=fake.paragraphs(nb=5),
        categoria=random.choice(categorias)
    )

print("✅ ¡Posts de prueba creados exitosamente!")