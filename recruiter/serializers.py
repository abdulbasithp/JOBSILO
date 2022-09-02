from rest_framework import serializers
from user.models import Account


class RecruiterProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = '__all__'
