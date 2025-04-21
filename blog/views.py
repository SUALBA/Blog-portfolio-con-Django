from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Post, Mensaje
from .forms import MensajeForm

def lista_posts(request):
    categoria = request.GET.get('categoria')
    posts_queryset = Post.objects.all().order_by('-fecha_publicacion')

    if categoria and categoria != 'all':
        posts_queryset = posts_queryset.filter(categoria=categoria)

    paginator = Paginator(posts_queryset, 6)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    return render(request, 'blog/lista_posts.html', {
        'posts': posts,
        'categoria_seleccionada': categoria or 'all',
    })


def sobre_mi(request):
    enviado = False

    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sobre-mi/?enviado=1')
    else:
        form = MensajeForm()
        if 'enviado' in request.GET:
            enviado = True

    mensajes_aprobados = Mensaje.objects.filter(aprobado=True).order_by('-fecha')

    return render(request, 'blog/sobre_mi.html', {
        'form': form,
        'enviado': enviado,
        'mensajes_aprobados': mensajes_aprobados,
    })


def lado_coder(request):
    posts = Post.objects.filter(categoria='code').order_by('-fecha_publicacion')
    return render(request, 'blog/lado_coder.html', {'posts': posts})
