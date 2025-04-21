from django.db import models
from django.utils import timezone

CATEGORIAS = [
    # Desarrollo Web
    ('html', 'HTML'),
    ('css', 'CSS'),
    ('js', 'JavaScript'),
    ('react', 'React'),
    ('vue', 'Vue'),
    ('angular', 'Angular'),
    ('backend', 'Backend'),
    ('docker', 'Docker'),
    ('terminal', 'Terminal y GitHub'),

    # Inteligencia Artificial
    ('chatgpt', 'ChatGPT'),
    ('ia', 'Inteligencia Artificial'),

    # Lenguajes
    ('python', 'Python'),

    # Ciberseguridad
    ('cyber', 'Cyberseguridad'),

    # StartUps y Productividad
    ('startup', 'StartUps'),
    ('excel', 'Excel'),
    ('salesforce', 'Salesforce'),

    # El lado Coder
    ('code', 'El lado Coder - Código de vida'),
]

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='html')

    def __str__(self):
        return self.titulo



class Mensaje(models.Model):
    nombre = models.CharField(max_length=100, blank=True)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    aprobado = models.BooleanField(default=False)

    def __str__(self):
        return f"Mensaje de {self.nombre or 'Anónimo'} - {self.fecha.strftime('%d/%m/%Y %H:%M')}"
