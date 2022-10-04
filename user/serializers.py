from rest_framework import serializers
from .models import Account
from rest_framework.validators import ValidationError
import re


class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = Account
        fields = ['first_name', 'middle_name', 'last_name', 'role', 'email', 'password']

    def validate(self, attrs):
        """"email validation"""
        email_exist = Account.objects.filter(email=attrs['email']).exists()
        if email_exist:
            raise ValidationError('The email is already exist')
        return super().validate(attrs)

    def validate_email(self, value):
        """
        Check that the email post is about Django.
        """
        pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
        if not re.match(pat,value):
            raise serializers.ValidationError("This is not a valid email, try again!")
        return value
    
    def create(self, validated_data):
        """hashing password"""
        password = validated_data.pop('password')

        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user


class UserViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'middle_name', 'email', 'phone_number', 'profile_image', 'dob', 'is_verified','city','role' ]

