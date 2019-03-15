from rest_framework import serializers
from django.contrib.auth.models import User
from apps.paises.models import Pais, Moneda

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ('id', 'iso', 'nombre', 'bandera', 'moneda', )
    
class MonedaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moneda
        fields = ('id', 'nombre', 'codigo_iso', 'simbolo', )