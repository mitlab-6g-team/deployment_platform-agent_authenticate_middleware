from main.apps.entrypoint.models.account import Account
from rest_framework import serializers

class AccountWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Account
        fields=['name', 'password']

class AccountReadSerializer(serializers.ModelSerializer):
    class Meta:
        model=Account
        fields='__all__'
