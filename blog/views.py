# blog/views.py

from django.urls import reverse_lazy
from django.views.generic import ListView, FormView
from django.contrib import messages
from django.core.mail import send_mail
from .models import Post, Mensaje
from .forms import MensajeForm

class PostListView(ListView):
    model = Post
    template_name = 'blog/lista_posts.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        qs = super().get_queryset().order_by('-fecha_publicacion')
        categoria = self.request.GET.get('categoria')
        if categoria and categoria != 'all':
            qs = qs.filter(categoria=categoria)
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['categoria_seleccionada'] = self.request.GET.get('categoria', 'all')
        return ctx


class SobreMiView(FormView):
    template_name = 'blog/sobre_mi.html'
    form_class = MensajeForm
    success_url = reverse_lazy('sobre_mi')  # asegúrate de tener el name="sobre_mi" en tu urls.py

    def form_valid(self, form):
        mensaje = form.save()
        # 1) Mensaje de éxito
        messages.success(self.request, '✅ ¡Gracias! Tu mensaje ha sido enviado correctamente.')
        # 2) Envío de correo al admin
        send_mail(
            subject=f'Nuevo mensaje de {mensaje.nombre or "Visitante"}',
            message=mensaje.mensaje,
            from_email=mensaje.email or 'noreply@tudominio.com',
            recipient_list=['tucorreo@tudominio.com'],
            fail_silently=True,
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        # En caso de AJAX/HTMX, devolvemos solo el fragmento del form con errores
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return self.render_to_response(self.get_context_data(form=form))
        # En caso normal, renderiza la página completa con errores inline
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['mensajes_aprobados'] = Mensaje.objects.filter(aprobado=True).order_by('-fecha')
        return ctx


class LadoCoderView(ListView):
    model = Post
    template_name = 'blog/lado_coder.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(categoria='code').order_by('-fecha_publicacion')
