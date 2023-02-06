from rest_framework import serializers
from .models import (AdminRegister)
from phonenumber_field.serializerfields import PhoneNumberField


class AddAdminSerializer(serializers.ModelSerializer):
    phone = PhoneNumberField(region="CA")

    class Meta:
        model = AdminRegister
        fields = ['name', 'email', 'phone']


class GetAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminRegister
        fields = ['name', 'email', 'phone', 'active']


class SendEmailSerializer(serializers.Serializer):
    recipient_list = serializers.EmailField()
