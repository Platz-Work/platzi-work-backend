
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated

from django.db import models
from .models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password


class RegisterSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['email'],
                                        password=validated_data['password'],
                                        name=validated_data['name']
                                       )
        return user

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'name')
        extra_kwargs = {
            'password': {'write_only': True},
        }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password','last_login','date_joined')
