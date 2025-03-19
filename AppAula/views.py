from django.shortcuts import render, get_object_or_404
from .models import Estudante, Professor, Curso, Entrega
from django.http import HttpResponse


def index(request):
    return HttpResponse("Olá, bem vindo ao APP Aula!")


def lista_estudantes(request):
    estudantes = Estudante.objects.all()
    return render(request, 'AppAula/estudantes_list.html', {'estudantes': estudantes})


def detalhe_estudante(request, pk):
    estudante = get_object_or_404(Estudante, pk=pk)
    return render(request, 'AppAula/estudante_detail.html', {'estudante': estudante})