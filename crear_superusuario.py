import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Aquí defines tu nuevo superusuario
username = "sualba"
email = "sualba.dev@gmail.com"
password = "Caramelo123"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print("✅ Superusuario creado correctamente.")
else:
    print("⚠️ El superusuario ya existe.")
