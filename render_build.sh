#!/usr/bin/env bash
set -e

# 1. Instala dependencias
pip install -r requirements.txt

# 2. Migra la base de datos
python manage.py migrate --noinput

# 3. Crea el superusuario en producción (si no existe)
python crear_superusuario.py

# 4. (Opcional) Crea posts de prueba (comentado porque ya no los necesitas)
# python manage.py create_fake_posts --count 30

# 5. Recopila estáticos
python manage.py collectstatic --noinput