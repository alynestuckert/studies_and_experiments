from django.contrib import admin
from .models import Estudante, Professor, Curso, Entrega, Post


admin.site.register(Estudante)
admin.site.register(Professor)
admin.site.register(Curso)
admin.site.register(Entrega)
# admin.site.register(Post)
@admin.register(Post)


class PostAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'data_publicacao']
    list_filter = [ 'autor']
    raw_id_fields = ['autor']
    ordering = ['-data_publicacao']
