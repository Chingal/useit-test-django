# -*- coding: utf-8 -*-
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    message = 'Debes ser dueño de este objeto.'

    def has_object_permission(self, request, view, obj):
        pass
        #return obj.user == request.user