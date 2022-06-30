from rest_framework import serializers
from .models import EnquiryForm, User
from django.contrib.auth.password_validation import validate_password
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
import re

from rest_framework import serializers
from .models import EnquiryForm

class EnquiryFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnquiryForm
        fields = '__all__'
    def create(self, validated_data):
        enquiry = EnquiryForm.objects.create(
        name=validated_data['name'],
        email=validated_data['email'],
        course=validated_data['course']
        )
        enquiry.save()
        return enquiry

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('Id', 'username', 'password', 'roleoftheUser')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.EmailField(required=True,validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    class Meta:
        model = User
        fields = ('Id', 'username', 'password', 'roleoftheUser')

    def validate(self, pass1):
        if not re.findall('\d{2,}', pass1['password']):
            raise serializers.ValidationError({"password": "The password must contain at least 2 digits."})

        if not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]{2,}', pass1['password']):
            raise serializers.ValidationError({"password": "The password must contain at least 2 special characters"})

        return pass1

    def create(self, validated_data):
        user = User.objects.create(
        username=validated_data['username'],
        password=validated_data['password'],
        roleoftheUser=validated_data['roleoftheUser']
        )
        user.save()
        return user






 
    