#!/usr/bin/env bash
# Archivo para migrar automáticamente en Render

python manage.py migrate
python manage.py collectstatic --noinput
