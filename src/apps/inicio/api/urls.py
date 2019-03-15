from django.urls import path
from .views import *

urlpatterns = [
    path('users/', UserList.as_view(), name=UserList.name),
    path('users/<int:pk>/', UserDetail.as_view(), name=UserDetail.name),
    path('boards/', BoardList.as_view(), name=BoardList.name),
    path('boards/<int:pk>/', BoardDetail.as_view(), name=BoardDetail.name),
    path('ideas/', IdeaList.as_view(), name=IdeaList.name),
    path('ideas/<int:pk>/', IdeaDetail.as_view(), name=IdeaDetail.name),
]