from dataclasses import fields
from pyexpat import model
from chat.chat import Chat
from chat.models import Intent
from rest_framework import serializers

class IntentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intent
        fields = '__all__'

class ChatSerializer(serializers.ModelSerializer):

    class Mata:
        model = Chat
        fields = "__all__"