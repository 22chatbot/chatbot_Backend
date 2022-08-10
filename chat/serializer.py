from dataclasses import fields
from pyexpat import model
from chat.models import Intenciones
from rest_framework import serializers

class IntencionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intenciones
        fields = '__all__'