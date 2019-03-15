# -*- coding: utf-8 -*-
from django import forms
from .models import *


#============= Formulario para el User =============
class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Usuario o email', 'class': 'form-control' }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '***********', 'class': 'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombres', 'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Apellidos', 'class': 'form-control'}))
    identificacion = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Número de Identificacion', 'class': 'form-control'}))
    foto     = forms.ImageField(required=False, label='Foto', widget=forms.ClearableFileInput())

    class Meta:
        model   = User
        exclude = ['username', 'password' ,'first_name', 'last_name', 'identificacion', 'foto', 'date_joined', ]


#============= Formulario para el Tablero =============
class BoardForm(forms.ModelForm):
    ESTADO = [
        ('PRIVADO', 'Privado'),
        ('PUBLICO', 'Público'),
    ]
    nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombre del Tablero', 'class': 'form-control mr-3'}))
    estado = forms.ChoiceField(label='Estado', widget=forms.Select(attrs={'class': 'custom-select mr-3'}), choices=ESTADO)

    class Meta:
        model   = Board
        fields = ['nombre', 'estado', ]
        exclude = ['propietario',]