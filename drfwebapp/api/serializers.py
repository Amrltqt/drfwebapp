# coding: utf-8

from django.contrib.auth.models import User
from rest_framework import serializers

from drfwebapp.models import Message


class MessageSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Message
        fields = ('id', 'content', 'created_at', 'owner')


class UserSerializer(serializers.ModelSerializer):

    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'messages')
        write_only_fields = ('password',)
        read_only_fields = ('id', )

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user