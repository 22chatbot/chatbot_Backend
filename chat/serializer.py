from dataclasses import fields
from chat.models import Intent
from rest_framework import serializers

class IntentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intent
        fields = '__all__'