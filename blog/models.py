from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify



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
    titulo            = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=False, unique=True)
    contenido         = models.TextField()
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    categoria         = models.CharField(max_length=20, choices=CATEGORIAS, default='html')
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
    nombre = models.CharField(max_length=100, blank=True)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    aprobado = models.BooleanField(default=False)

    def __str__(self):
        return f"Mensaje de {self.nombre or 'Anónimo'} - {self.fecha.strftime('%d/%m/%Y %H:%M')}"

