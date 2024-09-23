from main.apps.entrypoint.models.api import API
from rest_framework import serializers

class APItWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=API
        fields='__all__'

class APIReadSerializer(serializers.ModelSerializer):
    class Meta:
        model=API
        fields='__all__'
