# blog/models.py
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify


# 🛡️ Categorías del ecosistema sualba.dev
CATEGORIAS = [

    # 🔐 Ciberseguridad
    ('cyber', 'Ciberseguridad'),

    # 🔎 Inteligencia
    ('osint', 'OSINT'),

    # ⚔️ Seguridad ofensiva
    ('pentesting', 'Pentesting'),
    ('red-team', 'Red Team'),

    # 🛡️ Seguridad defensiva
    ('blue-team', 'Blue Team'),
    ('defensa', 'Defensa y Detección'),

    # 📜 Marcos normativos
    ('iso27001', 'ISO 27001'),
    ('ens', 'ENS (Esquema Nacional de Seguridad)'),
    ('nist', 'NIST CSF'),

    # 🔍 Auditoría y riesgos
    ('auditoria', 'Auditoría de Sistemas y Análisis de Riesgos'),
    ('grc', 'GRC y Cumplimiento'),
    ('riesgos', 'Gestión de Riesgos'),

    # 🔒 Privacidad
    ('privacidad', 'Privacidad por Diseño y Cumplimiento RGPD'),

    # 🧬 Investigación
    ('forense', 'Forense / DFIR'),

    # 🌐 Seguridad Web
    ('web', 'Seguridad Web'),

    # 🐍 Desarrollo y automatización
    ('python', 'Python: Automatización y Scripting de Seguridad'),
    ('desarrollo', 'Desarrollo'),

    # 🧠 IA
    ('ia', 'IA y Ciberseguridad'),

    # 🧪 Laboratorios
    ('laboratorio', 'Laboratorios'),

    # 🛠️ Producto propio
    ('auditsym', 'AuditSym'),

    # 🐳 Infraestructura
    ('devops', 'Docker y Despliegue Seguro (Render, Cloud)'),
    ('redes', 'Redes y Hardening de Sistemas'),

    # ✨ Se mantiene
    ('code', 'El lado Coder - Código de Vida'),
]


class Post(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=False, unique=True)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(default=timezone.now)

    categoria = models.CharField(
        max_length=20,
        choices=CATEGORIAS,
        default='cyber'
    )

    visitas = models.PositiveIntegerField(default=0)
    signals = models.PositiveIntegerField(default=0)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            'blog:detalle_post',
            kwargs={'slug': self.slug}
        )

    def get_categoria_emoji(self):
        emojis = {
            'cyber': '🔐',
            'osint': '🔎',
            'pentesting': '⚔️',
            'red-team': '🎯',
            'blue-team': '🛡️',
            'defensa': '🛡️',

            'iso27001': '📜',
            'ens': '🏛️',
            'nist': '📐',

            'auditoria': '🔍',
            'grc': '📋',
            'riesgos': '⚠️',

            'privacidad': '🔒',

            'forense': '🧬',

            'web': '🌐',

            'python': '🐍',
            'desarrollo': '💻',

            'ia': '🧠',

            'laboratorio': '🧪',

            'auditsym': '🛠️',

            'devops': '🐳',
            'redes': '🌐',

            'code': '✨',
        }

        return emojis.get(self.categoria, '◈')

    def __str__(self):
        return self.titulo


from django.db import models

class Mensaje(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(default="")  # ← Añade default=""
    motivo = models.CharField(
        max_length=100, 
        choices=[
            ('Auditoría / GRC', 'Auditoría / GRC'),
            ('AuditSym', 'AuditSym'),
            ('Colaboración', 'Colaboración'),
            ('Proyecto tecnológico', 'Proyecto tecnológico'),
            ('Formación / divulgación', 'Formación / divulgación'),
            ('Otro', 'Otro'),
        ],
        default='Otro'  # ← Añade default='Otro'
    )
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    aprobado = models.BooleanField(default=False)

    def __str__(self):
        return f"Mensaje de {self.nombre} - {self.motivo}"