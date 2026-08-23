from django.contrib import admin
from .models import Comentario, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'fecha_publicacion', 'visitas', 'signals')
    list_filter = ('categoria', 'fecha_publicacion')
    search_fields = ('titulo', 'contenido')
    prepopulated_fields = {'slug': ('titulo',)}
    date_hierarchy = 'fecha_publicacion'

from .models import Mensaje

@admin.register(Mensaje)
class MensajeAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha', 'aprobado')
    list_filter = ('aprobado', 'fecha')
    search_fields = ('nombre', 'mensaje')
    list_editable = ('aprobado',)


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'post',
        'fecha',
        'autoriza_mencion',
        'aprobado',
    )
    list_filter = ('aprobado', 'autoriza_mencion', 'fecha')
    search_fields = ('nombre', 'email', 'contenido', 'post__titulo')
    list_editable = ('aprobado',)
    readonly_fields = ('fecha',)
    actions = ('aprobar_comentarios',)

    @admin.action(description='Aprobar los comentarios seleccionados')
    def aprobar_comentarios(self, request, queryset):
        queryset.update(aprobado=True)