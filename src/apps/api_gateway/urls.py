from django.urls import path, include
from .views import ApiRoot

urlpatterns = [
    path('', ApiRoot.as_view(), name=ApiRoot.name),
    path('', include('apps.inicio.api.urls')),
]