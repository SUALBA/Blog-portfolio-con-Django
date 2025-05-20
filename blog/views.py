from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, DetailView
from django.contrib import messages
from django.core.mail import send_mail
from .models import Post
from .forms import MensajeForm

# Categorías válidas para validación
CATEGORIAS_VALIDAS = {
    'html', 'css', 'js', 'react', 'vue', 'angular', 'backend',
    'docker', 'terminal', 'python', 'chatgpt', 'ia', 'cyber',
    'startup', 'excel', 'salesforce', 'code', 'all'
}

class DetallePostView(DetailView):
    model = Post
    template_name = 'blog/detalle_post.html'  # Corregir template
    context_object_name = 'post'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.visitas += 1
        obj.save(update_fields=['visitas'])
        return obj

class PostListView(ListView):
    model = Post
    template_name = 'blog/lista_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        categoria = self.request.GET.get('categoria', 'all').lower()
        
        # Validar y filtrar categoría
        if categoria not in CATEGORIAS_VALIDAS:
            categoria = 'all'
            
        qs = super().get_queryset().order_by('-fecha_publicacion')
        
        if categoria != 'all':
            qs = qs.filter(categoria=categoria)
        
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categoria = self.request.GET.get('categoria', 'all').lower()
        
        # Asegurar categoría válida en contexto
        context['categoria_seleccionada'] = categoria if categoria in CATEGORIAS_VALIDAS else 'all'
        
        # Lógica optimizada para posts populares
        populares = Post.objects.order_by('-visitas')[:5]
        if not populares.exists():
            populares = Post.objects.order_by('-fecha_publicacion')[:5]
        
        context['populares'] = populares
        return context

class SobreMiView(FormView):
    template_name = 'blog/sobre_mi.html'
    form_class = MensajeForm
    success_url = reverse_lazy('sobre_mi')

    def form_valid(self, form):
        mensaje = form.save()
        messages.success(self.request, '✅ ¡Gracias! Tu mensaje ha sido enviado correctamente.')
        send_mail(
            subject=f'Nuevo mensaje de {mensaje.nombre or "Visitante"}',
            message=mensaje.mensaje,
            from_email=mensaje.email or 'noreply@tudominio.com',
            recipient_list=['tucorreo@tudominio.com'],
            fail_silently=True,
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return self.render_to_response(self.get_context_data(form=form))
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['categoria_seleccionada'] = self.request.GET.get('categoria', 'all')
        ctx['populares'] = Post.objects.order_by('-visitas')[:5]
        return ctx


class LadoCoderView(ListView):
    model = Post
    template_name = 'blog/lado_coder.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(categoria='code').order_by('-fecha_publicacion')