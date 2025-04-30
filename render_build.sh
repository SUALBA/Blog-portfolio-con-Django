#!/usr/bin/env bash
# Archivo para migrar automáticamente en Render
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput


