from django import forms
from .models import Estudante, Post, Curso
from .models import User, Avatar
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import PasswordChangeForm

class EstudanteForm(forms.ModelForm):
    class Meta:
        model = Estudante
        fields = ['nome', 'sobrenome', 'email']

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['curso', 'turma', 'data_inicio', 'data_fim']
        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
            'data_fim': forms.DateInput(attrs={'type': 'date'}),
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'conteudo','curso_turma']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'conteudo': forms.Textarea(attrs={'class': 'form-control'}),
            'curso_turma': forms.Select(attrs={'class': 'form-select'}),
        }

class PesquisaEstudanteForm(forms.Form):
    termo = forms.CharField(
        label="Pesquisar estudante",
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite nome ou sobrenome'})
    )

class PesquisaCursoForm(forms.Form):
    termo = forms.CharField(
        label="Pesquisar curso",
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite nome do curso'})
    )


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ['username', 'email', 'password']


    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise ValidationError('A senha deve ter pelo menos 8 caracteres.')
        if not any(char.isdigit() for char in password):
            raise ValidationError('A senha deve conter pelo menos um número.')
        if not any(char.isupper() for char in password):
            raise ValidationError('A senha deve conter pelo menos uma letra maiúscula.')
        return password


    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')


        if password != password_confirm:
            raise ValidationError('As senhas não coincidem.')
        return password_confirm



class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']  


class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagem']