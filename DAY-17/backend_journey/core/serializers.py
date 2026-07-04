from rest_framework import serializers
from .models import Student
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields =  ['id', 'name', 'email', 'age', 'course']

    def validate_age(self, value):
        if value < 18:
            raise serializers.ValidationError(
                "Student must be at least 18 years old."
            )
        return value
    
    def validate_email(self, value):
        if Student.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "Email already exists."
            )
        return value
    
    def validate_name(self, value):
        if any(char.isdigit() for char in value):
            raise serializers.ValidationError(
                "Name cannot contain numbers."
            )
        return value
    
    def validate_course(self, value):
       if not value.strip():
            raise serializers.ValidationError(
                "Course cannot be empty."
            )
       return value

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=8
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError(
                "Username already exists."
            )
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "Email already exists."
            )
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
            # Check whether username exists
            from django.contrib.auth.models import User

            if not User.objects.filter(username=username).exists():
                raise serializers.ValidationError(
                    {"username": "Username does not exist."}
                )

            raise serializers.ValidationError(
                {"password": "Incorrect password."}
            )

        refresh = RefreshToken.for_user(user)

        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
    
class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', 'date_joined']

