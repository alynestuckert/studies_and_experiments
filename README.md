# 📘 Projeto Final

A aplicação que está em Projeto Final tem o objetivo de criar uma página de gerenciamento para a empresa ASF Cursos, permitindo criação de posts, cadastro de estudantes e controle por turmas e cursos.

---

## 🚀 Tecnologias Utilizadas

- [Python 3.10.12](https://www.python.org/)
- [Django 5.2](https://www.djangoproject.com/)
- SQLite
- HTML + Bootstrap (interface)
- Outros pacotes (listados no `requirements.txt`)

---

## ⚙️ Instalação

1. **Clone o repositório:**

```bash
git clone https://github.com/alynestuckert/studies_and_experiments.git
```
2. **Crie e ative um ambiente virtual:**
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

4. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

6. Inicie o servidor:
```bash
python manage.py runserver
```
Acesse: http://127.0.0.1:8000/

## 🗂️ Estrutura do Projeto
```bash
coder_house/Projeto Final/
  ├── AppAula
  │   ├── admin.py
  │   ├── apps.py
  │   ├── forms.py
  │   ├── __init__.py
  │   ├── models.py
  │   ├── templates
  │   │   ├── AppAula
  │   │   │   ├── atualizar_post.html
  │   │   │   ├── confirmar_deletar_post.html
  │   │   │   ├── criar_curso.html
  │   │   │   ├── criar_estudante.html
  │   │   │   ├── criar_post.html
  │   │   │   ├── curso_detail.html
  │   │   │   ├── curso_list.html
  │   │   │   ├── detalhe_post.html
  │   │   │   ├── editar_perfil.html
  │   │   │   ├── estudante_detail.html
  │   │   │   ├── estudantes_list.html
  │   │   │   ├── lista_posts.html
  │   │   │   ├── logout.html
  │   │   │   ├── perfil.html
  │   │   │   ├── pesquisa_curso.html
  │   │   │   ├── pesquisa_estudante.html
  │   │   │   ├── post_delete.html
  │   │   │   ├── post_detail.html
  │   │   │   ├── post_edit.html
  │   │   │   ├── post_form.html
  │   │   │   ├── post_list.html
  │   │   │   ├── registration.html
  │   │   │   ├── sobre.html
  │   │   │   └── upload_avatar.html
  │   │   ├── base.html
  │   │   └── registration
  │   │       └── login.html
  │   ├── tests.py
  │   ├── urls.py
  │   └── views.py
  ├── home
  │   ├── admin.py
  │   ├── apps.py
  │   ├── __init__.py
  │   ├── models.py
  │   ├── templates
  │   │   └── home
  │   │       └── index.html
  │   ├── tests.py
  │   ├── urls.py
  │   └── views.py
  ├── manage.py
  ├── on_delete.ipynb
  │   ├── include
  │   ├── lib
  │   │   └── python3.10
  │   │       └── site-packages
  │   ├── lib64 -> lib
  │   └── pyvenv.cfg
  ├── ProjetoDjango70930
  │   ├── asgi.py
  │   ├── __init__.py
  │   ├── settings.py
  │   ├── urls.py
  │   └── wsgi.py
  └── requirements.txt
```

## ✍️ Funcionalidades
- Cadastro de Estudantes
- Cadastros de Cursos
- Cadtastros de Atividades
- Cadastro de usuários
- Login e senha para responsáveis de postagens
- Gerenciamento pelo Admin Django



