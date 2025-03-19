from django.contrib import admin
from .models import Estudante, Professor, Curso, Entrega


admin.site.register(Estudante)
admin.site.register(Professor)
admin.site.register(Curso)
admin.site.register(Entrega)
