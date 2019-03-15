from django.conf import settings
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from apps.api_gateway.permissions import IsOwnerOrReadOnly
from apps.api_gateway.pagination import AppLimitOffsetPagination, AppPageNumberPagination

from apps.inicio.models import User
from .serializers import *


class UserList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    name = 'User List'
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    pagination_class = AppPageNumberPagination
    queryset = User.objects.all().order_by('id')


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'User Detail'
    lookup_field = 'pk'
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated, ]


class BoardList(generics.ListCreateAPIView):
    serializer_class = BoardSerializer
    name = 'Board List'
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated, ]
    pagination_class = AppPageNumberPagination
    queryset = Board.objects.all().order_by('id')

    def perform_create(self, serializer):
        serializer.save(propietario=self.request.user)


class BoardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    name = 'Board Detail'
    lookup_field = 'pk'
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated, ]


class IdeaList(generics.ListCreateAPIView):
    serializer_class = IdeaSerializer
    name = 'Idea List'
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated, ]
    pagination_class = AppPageNumberPagination
    queryset = Idea.objects.all().order_by('id')


class IdeaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer
    name = 'Idea Detail'
    lookup_field = 'pk'
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated, ]