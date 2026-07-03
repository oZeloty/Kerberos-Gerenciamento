from django.shortcuts import render, get_object_or_404
from .models import Usuario, Pet


def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    contexto = {'usuarios': usuarios}
    return render(request, 'usuario/listar_usuarios.html', contexto)