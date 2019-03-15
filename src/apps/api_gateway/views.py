from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.reverse import reverse

from apps.inicio.api.views import UserList, BoardList, IdeaList

class ApiRoot(generics.GenericAPIView):
    name = 'Api Root'
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        return Response({
            'users': reverse(UserList.name, request=request),
            'boards': reverse(BoardList.name, request=request),
            'ideas': reverse(IdeaList.name, request=request),
        })