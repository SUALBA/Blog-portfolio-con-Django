from django.contrib import admin
from .models import Post

admin.site.register(Post)

from django.contrib import admin
from .models import Mensaje

@admin.register(Mensaje)
class MensajeAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha', 'aprobado')
    list_filter = ('aprobado', 'fecha')
    search_fields = ('nombre', 'mensaje')
    list_editable = ('aprobado',)
