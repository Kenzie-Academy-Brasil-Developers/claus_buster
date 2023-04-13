from rest_framework import serializers, status
from .models import User
from rest_framework.response import Response
from ptpdb import set_trace
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=127, validators=[UniqueValidator(
        queryset=User.objects.all(),
        message='username already taken.'
    )])
    email = serializers.EmailField(max_length=127, validators=[UniqueValidator(
        queryset=User.objects.all(),
        message='email already registered.'
    )])
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    birthdate = serializers.DateField(default=None)
    is_employee = serializers.BooleanField(default=False)
    is_superuser = serializers.BooleanField(default=False, read_only=True)
    password = serializers.CharField(max_length=127, write_only=True)

    def create(self, validated_data: dict) -> User:
        if validated_data['is_employee']:
            validated_data['is_superuser'] = True
        return User.objects.create_user(**validated_data)
