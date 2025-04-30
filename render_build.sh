#!/usr/bin/env bash
set -e

# 1. Instala dependencias
pip install -r requirements.txt

# 2. Migra la base de datos
python manage.py migrate --noinput

# 3. Crea posts de prueba en producción
python manage.py create_fake_posts --count 30

# 4. Recopila estáticos
python manage.py collectstatic --noinput
