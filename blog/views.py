
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, DetailView
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import ComentarioForm, MensajeForm, ContactoForm
from .models import Post, CATEGORIAS
from django.http import JsonResponse
from django.views.decorators.http import require_POST

# Categorías válidas
CATEGORIAS_VALIDAS = {slug for slug, _ in CATEGORIAS}
CATEGORIAS_VALIDAS.add('all')
def home_view(request):
    populares = Post.objects.order_by('-visitas')[:5]

    if not populares.exists():
        populares = Post.objects.order_by('-fecha_publicacion')[:5]

    return render(
        request,
        'blog/home.html',
        {
            'populares': populares,
        }
    )
class DetallePostView(DetailView):
    model = Post
    template_name = 'blog/detalle_post.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if self.request.method == 'GET':
            obj.visitas += 1
            obj.save(update_fields=['visitas'])
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['es_codigo_de_vida'] = self.object.categoria == 'code'
        if context['es_codigo_de_vida']:
            context['comentarios'] = self.object.comentarios.filter(aprobado=True)
            context['comentario_form'] = kwargs.get(
                'comentario_form',
                ComentarioForm()
            )
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.object.categoria != 'code':
            messages.error(
                request,
                'Los comentarios están disponibles en Código de Vida.'
            )
            return redirect(self.object.get_absolute_url())

        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = self.object
            comentario.save()

            send_mail(
                subject=f'Nueva opinión pendiente en: {self.object.titulo}',
                message=(
                    f'Nombre o alias: {comentario.nombre}\n'
                    f'Email: {comentario.email}\n'
                    f'Autoriza mención: {"Sí" if comentario.autoriza_mencion else "No"}\n\n'
                    f'Comentario:\n{comentario.contenido}'
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['sualba.dev@gmail.com'],
                fail_silently=True,
            )
            messages.success(
                request,
                '💫 Gracias por participar. Tu opinión se publicará después de ser revisada.'
            )
            return redirect(f'{self.object.get_absolute_url()}#conversacion')

        context = self.get_context_data(comentario_form=form)
        return self.render_to_response(context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/lista_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset().order_by('-fecha_publicacion')
        categoria = self.request.GET.get('categoria', 'all')
        if categoria != 'all' and categoria in CATEGORIAS_VALIDAS:
            qs = qs.filter(categoria=categoria)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Diccionario de emojis para cada categoría
        emojis = {
            'cyber': '🔐', 'osint': '🔎', 'pentesting': '⚔️',
            'red-team': '🎯', 'blue-team': '🛡️', 'grc': '📋',
            'auditoria': '🔍', 'riesgos': '⚠️', 'forense': '🧬',
            'python': '🐍', 'ia': '🧠', 'laboratorio': '🧪',
            'web': '🌐', 'defensa': '🛡️', 'desarrollo': '💻',
            'code': '🧘',
        }
        # Crear lista de categorías con su emoji
        categorias_con_iconos = [(slug, nombre, emojis.get(slug, '◈')) for slug, nombre in CATEGORIAS]
        context['categorias'] = categorias_con_iconos
        context['categoria_seleccionada'] = self.request.GET.get('categoria', 'all')

        # Populares
        populares = Post.objects.order_by('-visitas')[:5]
        if not populares.exists():
            populares = Post.objects.order_by('-fecha_publicacion')[:5]
        context['populares'] = populares

        return context


class SobreMiView(FormView):
    template_name = 'blog/sobre_mi.html'
    form_class = MensajeForm
    success_url = None

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['categoria_seleccionada'] = self.request.GET.get('categoria', 'all')
        ctx['populares'] = Post.objects.order_by('-visitas')[:5]
        return ctx

    def form_valid(self, form):
        mensaje = form.save()
        messages.success(self.request, '✅ ¡Gracias! Tu mensaje ha sido enviado correctamente desde Sobre mí.')
        send_mail(
            subject=f'Nuevo mensaje de {mensaje.nombre or "Visitante"} en sualba.dev (Sobre mí)',
            message=f'Nombre: {mensaje.nombre}\nEmail: {mensaje.email}\n\nMensaje:\n{mensaje.mensaje}',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['sualba.dev@gmail.com'],
            fail_silently=True,
        )
        return super().form_valid(form)


class LadoCoderView(ListView):
    model = Post
    template_name = 'blog/lado_coder.html'
    context_object_name = 'posts'
    paginate_by = 7

    def get_queryset(self):
        return Post.objects.filter(categoria='code').order_by('-fecha_publicacion')


def contacto_view(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            mensaje = form.save()
            asunto = f"Nuevo contacto web: {mensaje.motivo} - {mensaje.nombre}"
            cuerpo = f"Nombre: {mensaje.nombre}\nEmail: {mensaje.email}\nMotivo: {mensaje.motivo}\n\nMensaje:\n{mensaje.mensaje}"
            send_mail(
                subject=asunto,
                message=cuerpo,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['sualba.dev@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, "¡Mensaje enviado con éxito! Te responderé pronto.")
            return redirect('blog:contacto')
    else:
        form = ContactoForm()
    return render(request, 'blog/contacto.html', {'form': form})

def proyectos(request):
    """
    Vista para la página de proyectos / casos de estudio.
    """
    return render(request, 'blog/proyectos.html')

@require_POST
def signal_post(request, pk):
    try:
        post = Post.objects.get(pk=pk)
        post.signals += 1
        post.save(update_fields=['signals'])

        return JsonResponse({
            'ok': True,
            'signals': post.signals
        })

    except Post.DoesNotExist:
        return JsonResponse({'ok': False}, status=404)