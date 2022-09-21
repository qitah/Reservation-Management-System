from .models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'employee_number', 'password']

        extra_kwargs = {
        'password': {'write_only': True},
        }
