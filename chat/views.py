from rest_framework.decorators import action
from email import message
from importlib.resources import Resource
from typing import List
from rest_framework.response import Response
from rest_framework.request import Request
from chat.chat import Chat
from chat.models import Intent
from rest_framework import viewsets
from chat.serializer import IntentSerializer
from chat.train import Train

class IntentViewSet(viewsets.ModelViewSet):
    serializer_class = IntentSerializer
    queryset = Intent.objects.all()

    @action(detail=True, methods=['post'])
    def train(self, request, *args, **kwargs):

        trainer = Train()
        trainer.toTrain(list(Intent.objects.values()))
        return Response({'train':'Ok'})

    @action(detail=True, methods=['post'])
    def ask(self, request: Request, *args, **kwargs):
        print("Atendiendo preguntas")
        data = JSONParser().parse(request)
        serializer = serializers.ChatSerializer(data=data)
        if serializer.is_valid():
            ask_message = serializer.data.get("message")
            chat = Chat(list(Intent.objects.values()))
            message = chat.begin(ask_message)
            return Response({'message':message, 'userType':'AGENT'})
        return Response({'message':'SIN RESPUESTA', 'userType':'AGENT'})