import requests
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import View
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .forms import *
from .models import *

@method_decorator(login_required, name='dispatch')
class Home(View):
    name = 'home'
    template_name = 'inicio/home.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated and not request.user.is_superuser:
            boards = Board.objects.filter(propietario=request.user)
            public_boards = Board.objects.filter(estado='PUBLICO').exclude(propietario=request.user)
            form_board = BoardForm()
        else:
            return redirect('admin:index')
        return render(request, self.template_name, locals())

    def post(self, request, *args, **kwargs):
        user = User.objects.get(username=request.user)
        form_board = BoardForm(request.POST)
        if form_board.is_valid():
            board = form_board.save(commit=False)
            board.nombre = request.POST.get('nombre')
            board.estado = request.POST.get('estado')
            board.propietario = user
            board.save()
            return redirect('home')
        return render(request, self.template_name, locals())


class ReigistrarUsuario(CreateView):
    name = 'register'
    form_class = UserForm
    model = User
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        form = UserForm(None, request.FILES or None)
        return render(request, self.template_name, locals())

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST, request.FILES)
        if (form.is_valid()):
            usuario = form.save(commit=False)
            usuario.username = request.POST.get('username')
            usuario.set_password(request.POST.get('password'))
            usuario.first_name = request.POST.get('first_name')
            usuario.last_name = request.POST.get('last_name')
            usuario.identificacion = request.POST.get('identificacion')
            usuario.is_active = True
            if 'foto' in request.FILES:
                usuario.foto = request.FILES['foto']
            usuario.save()
            #sweetify.success(self.request, 'Lo hiciste', text='Muy bien! Información Almacenada', persistent="Ok")
            return redirect(self.success_url)
        return render(request, self.template_name, locals())


@method_decorator(login_required, name='dispatch')
class EliminarTablero(View):
    name = 'delete-board'
    model = Board
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        board = Board.objects.get(pk=kwargs['pk'])
        if board:
            board.delete()
        return redirect(self.success_url)
