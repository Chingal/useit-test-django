from rest_framework import serializers
from apps.inicio.models import *

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'identificacion', )

    # is called if we save serializer if it do not have an instance
    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create(**validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user


class BoardSerializer(serializers.ModelSerializer):
    propietario = serializers.SerializerMethodField()
    ideas = serializers.SerializerMethodField()

    class Meta:
        model = Board
        fields = ('id', 'nombre', 'estado', 'propietario', 'ideas', )

    def get_propietario(self, obj):
        return obj.propietario.username

    def get_ideas(self, obj):
        ideas = obj.ideas.all()
        return IdeaSerializer(ideas, many=True).data


class IdeaSerializer(serializers.ModelSerializer):
    board = serializers.SlugRelatedField(queryset=Board.objects.all(), slug_field='id')

    class Meta:
        model = Idea
        fields = ('id', 'nombre', 'estado', 'board', )