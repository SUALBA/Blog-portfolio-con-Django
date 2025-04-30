from django.core.management.base import BaseCommand
from blog.models import Post
from faker import Faker
import random
from django.utils import timezone

CATEGORIAS = [c[0] for c in Post._meta.get_field('categoria').choices]

class Command(BaseCommand):
    help = "Crea N posts de prueba con Faker"

    def add_arguments(self, parser):
        parser.add_argument(
            '--count', '-c',
            type=int,
            default=10,
            help="Cuántos posts generar",
        )

    def handle(self, *args, **options):
        fake = Faker()
        count = options['count']
        for i in range(count):
            Post.objects.create(
                titulo=fake.sentence(nb_words=6),
                contenido="\n\n".join(fake.paragraphs(nb=5)),
                fecha_publicacion=timezone.now(),
                categoria=random.choice(CATEGORIAS),
            )
        self.stdout.write(self.style.SUCCESS(
            f"✅ Generados {count} posts de prueba"
        ))
