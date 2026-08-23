from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Comentario, Post


class ComentariosCodigoDeVidaTests(TestCase):
    def setUp(self):
        self.post_vida = Post.objects.create(
            titulo='Una reflexión',
            slug='una-reflexion',
            contenido='Contenido humano',
            categoria='code',
            fecha_publicacion=timezone.now(),
        )
        self.post_tecnico = Post.objects.create(
            titulo='Artículo técnico',
            slug='articulo-tecnico',
            contenido='Contenido técnico',
            categoria='cyber',
            fecha_publicacion=timezone.now(),
        )

    def test_comentario_valido_se_guarda_pendiente(self):
        response = self.client.post(
            reverse('blog:detalle_post', kwargs={'slug': self.post_vida.slug}),
            {
                'nombre': 'Lectora',
                'email': 'lectora@example.com',
                'contenido': 'Una aportación interesante.',
                'autoriza_mencion': 'on',
                'privacidad': 'on',
                'website': '',
            },
        )

        self.assertEqual(response.status_code, 302)
        comentario = Comentario.objects.get()
        self.assertFalse(comentario.aprobado)
        self.assertTrue(comentario.autoriza_mencion)
        self.assertEqual(comentario.post, self.post_vida)

    def test_no_admite_comentarios_en_posts_tecnicos(self):
        response = self.client.post(
            reverse('blog:detalle_post', kwargs={'slug': self.post_tecnico.slug}),
            {
                'nombre': 'Lectora',
                'email': 'lectora@example.com',
                'contenido': 'Comentario',
                'privacidad': 'on',
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Comentario.objects.exists())

    def test_solo_muestra_comentarios_aprobados(self):
        Comentario.objects.create(
            post=self.post_vida,
            nombre='Visible',
            email='visible@example.com',
            contenido='Comentario aprobado',
            aprobado=True,
        )
        Comentario.objects.create(
            post=self.post_vida,
            nombre='Pendiente',
            email='pendiente@example.com',
            contenido='Comentario pendiente',
            aprobado=False,
        )

        response = self.client.get(
            reverse('blog:detalle_post', kwargs={'slug': self.post_vida.slug})
        )

        self.assertContains(response, 'Comentario aprobado')
        self.assertNotContains(response, 'Comentario pendiente')

# Create your tests here.