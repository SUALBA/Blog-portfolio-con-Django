# 🌐 sualba.dev - Blog personal y portfolio

Bienvenido a mi proyecto de Blog + Portfolio personal, desarrollado con **Django 5.2** y desplegado en **Render**.

Este espacio es donde comparto:
- 📚 Mis aprendizajes sobre desarrollo web, programación y ciberseguridad.
- 👨‍💻 Mis proyectos y experiencias personales en el mundo tech.
- ✨ Reflexiones personales en la sección especial **"Código de Vida"**.

---

## 🚀 ¿Qué encontrarás aquí?

📝 Un blog categorizado sobre:

- Desarrollo Web
- Frontend : HTML, CSS y JS
- React, Vue y Angular
- Backend & Docker
- Terminal & GitHub
- Python y ChatGPT
- Inteligencia Artificial
- Startups y Salesforce
- Excel y Marketing
- Cyberseguridad 🔐
- ☕ El lado Coder (reflexiones y código de vida)

---

## ✨ Tecnologías utilizadas

- **Python 3.13** 🐍
- **Django 5.2** 🌿
- HTML + CSS personalizados
- Paginación, filtros por categoría y lógica backend
- Panel de administración para gestión de contenido
- Formularios validados con aprobación manual
- PostgreSQL (base de datos en producción)
- Gunicorn (servidor WSGI)
- WhiteNoise (para servir archivos estáticos)
- Render.com (hosting gratuito)
- GitHub (repositorio y control de versiones)

---
## 📂 Estructura del Proyecto

```bash
blog-portfolio/
├── blog/           # App principal: posts, categorías, código de vida
├── config/         # Configuración global del proyecto Django
├── static/         # Archivos estáticos (CSS, imágenes, JS)
├── templates/      # Plantillas HTML
├── requirements.txt
├── render.yaml
├── render_build.sh
├── .env            # Variables de entorno (local)
├── .gitignore
├── README.md
└── manage.py

## 📸 Captura del sitio

screenshotblog.png

> Puedes ver la evolución de este proyecto en tiempo real. ¡Estoy aprendiendo y construyendo al mismo tiempo!

---

## 👤 Sobre mí

Soy desarrolladora web apasionada por la tecnología, el diseño, la inteligencia artificial y la ciberseguridad.  
Actualmente enfocada en construir herramientas que mezclen código y creatividad.

🔗 [Mi blog: sualba.dev](https://sualba.dev)  
🐙 [GitHub: SUALBA](https://github.com/SUALBA)

---

## 📩 Contacto

Si quieres dejarme un mensaje o sugerencia, puedes hacerlo desde la sección **Sobre mí** en el blog 😉

---

## 💻 Cómo levantarlo en local 🚀 
1.Clona el repositorio:
```bash
git clone https://github.com/SUALBA/Blog-portfolio-con-Django.git
cd Blog-portfolio-con-Django

2. Crea y activa un entorno virtual:
```bash
python -m venv env
source env/bin/activate   # en Linux/Mac
env\Scripts\activate.bat  # en WindowsWindows

3. Instala dependencias:
```bash
pip install -r requirements.txt
pip install django-admin-interface
python manage.py migrate

4. Configura variables de entorno locales en .env.

5. Lanza el servidor:
``bash
python manage.py runserver

🔥 Despliegue en Producción
El proyecto está desplegado automáticamente en Render.com.
Para el despliegue:

Utiliza un render.yaml bien estructurado.

Usa PostgreSQL como base de datos.

Sirve estáticos con WhiteNoise.

Lee la base de datos de la variable DATABASE_URL (gracias a dj-database-url).

💬 ¿Por qué Django y PostgreSQL?
Django + PostgreSQL son una pareja robusta, segura y profesional.

Usar dj-database-url me permite cambiar de hosting sin tocar el código, solo configurando una variable de entorno.

🎯 Objetivos
Mostrar mi pasión por el desarrollo web y la ciberseguridad.

Construir una marca personal sólida en internet.

Demostrar habilidades técnicas, abierta a ofertas reales de cara a recruiters🎯.

🎨 Mejoras en el Admin de Django
He integrado un tema moderno en el Admin con django-admin-interface:

Tema oscuro

Botones estilizados

Layout espacioso

Colores personalizables

Mejor experiencia de administración

📬 Contacto
Si quieres contactarme, puedes hacerlo en sualba.dev o a través de mis redes.
PD: ¡Gracias por visitar mi proyecto! 🚀 Espero que encuentres inspiración aquí.