# coding: utf-8

from .models import Message
from django.contrib.auth.models import User
from rest_framework import serializers


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ('id', 'content', 'created_at')


class UserSerializer(serializers.ModelSerializer):

    message = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('username', 'messages')