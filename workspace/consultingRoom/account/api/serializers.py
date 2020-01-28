from rest_framework import serializers
from datetime import datetime, date, time, timedelta
from rest_framework.validators import (
    UniqueValidator,
    UniqueForDateValidator,
    UniqueTogetherValidator
)

from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError(
                'Users must have an email address')
        else:
            try:
                user = User.objects.get(email=value)
                raise serializers.ValidationError(
                    'A user with that email already exists.')
            except User.DoesNotExist:
                pass
        return value

    def create(self, validated_data):

        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password'],)
        return user

    class Meta:
        model = User
        fields = '__all__'
