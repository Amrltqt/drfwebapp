# coding: utf-8

from django.contrib.auth import get_user_model

from rest_framework import generics
from rest_framework import permissions
from drfwebapp.api.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer


