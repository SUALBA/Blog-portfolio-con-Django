# blog/models.py
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify


# 🎯 Categorías alineadas con tus Áreas de Especialización
CATEGORIAS = [
    # 📜 Marcos Normativos
    ('iso27001', 'ISO 27001'),
    ('ens', 'ENS (Esquema Nacional de Seguridad)'),
    ('nist', 'NIST CSF'),

    # 🔍 Auditoría y riesgos
    ('auditoria', 'Auditoría de Sistemas y Análisis de Riesgos'),

    # 🔒 Privacidad
    ('privacidad', 'Privacidad por Diseño y Cumplimiento RGPD'),

    # 🛠️ Herramientas propias
    ('auditsym', 'AuditSym'),

    # 🐍 Automatización
    ('python', 'Python: Automatización y Scripting de Seguridad'),

    # ⚙️ Arquitectura Web
    ('web', 'Arquitectura Web (React, Node.js, Django)'),

    # 🐳 Despliegue seguro
    ('devops', 'Docker y Despliegue Seguro (Render, Cloud)'),

    # 🌐 Redes
    ('redes', 'Gestión de Redes y Hardening de Sistemas'),

    # ✨ El lado Coder (NO borrar: LadoCoderView filtra por 'code')
    ('code', 'El lado Coder - Código de vida'),
]


class Post(models.Model):
    titulo            = models.CharField(max_length=200)
    slug              = models.SlugField(max_length=200, blank=False, unique=True)
    contenido         = models.TextField()
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    # ✅ default actualizado: 'html' ya no existe
    categoria         = models.CharField(max_length=20, choices=CATEGORIAS, default='auditoria')
    visitas           = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        # Usa el namespace 'blog' y el slug
        return reverse('blog:detalle_post', kwargs={'slug': self.slug})

    def __str__(self):
        return self.titulo


class Mensaje(models.Model):
    nombre   = models.CharField(max_length=100, blank=True)
    mensaje  = models.TextField()
    fecha    = models.DateTimeField(auto_now_add=True)
    aprobado = models.BooleanField(default=False)

    def __str__(self):
        return f"Mensaje de {self.nombre or 'Anónimo'} - {self.fecha.strftime('%d/%m/%Y %H:%M')}"