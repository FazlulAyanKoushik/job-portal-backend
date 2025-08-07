from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import User
from .utils import validate_password_strength


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password_strength])
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'role', 'password', 'confirm_password')

    def validate(self, data) -> dict:
        if not data['password']:
            raise serializers.ValidationError("Password is required.")
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    @staticmethod
    def validate_role(value: str) -> str:
        if value.upper() == 'ADMIN':
            raise serializers.ValidationError("Admin registration is not allowed.")
        return value

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(email=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        if not user.is_active:
            raise serializers.ValidationError("User is inactive")
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'role']
