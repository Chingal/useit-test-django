from django.urls import path
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    path('home/', Home.as_view(), name=Home.name),
    path('register/', ReigistrarUsuario.as_view() , name=ReigistrarUsuario.name),
    path('home/<int:pk>/', EliminarTablero.as_view(), name=EliminarTablero.name),
]
