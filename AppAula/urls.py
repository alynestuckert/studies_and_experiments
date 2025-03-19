from django.urls import include, path
from .views import lista_estudantes, detalhe_estudante


urlpatterns = [
    path('estudantes/', lista_estudantes, name='lista_estudantes'),
    path('estudantes/<int:pk>/', detalhe_estudante, name='detalhe_estudante'),
]
