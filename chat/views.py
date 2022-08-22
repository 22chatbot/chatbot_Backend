from argparse import Action
from crypt import methods
from email import message
from importlib.resources import Resource
from typing import List
from urllib import response
from urllib.request import Request
from chat.chat import Chat
from chat.models import Intent
from rest_framework import viewsets
from chat.serializer import IntentSerializer
from chat.train import Train

class IntentViewSet(viewsets.ModelViewSet):
    serializer_class = IntentSerializer
    queryset = Intent.objects.all()

    @Action(detail=True, methods=['post'])
    def train(self, request, *args, **kwargs):

        trainer = Train()
        trainer.toTrain(list(Intent.objects.values()))
        return response({'train':'Ok'})

    @action(detail=True, methods=['post'])
    def ask(self, request: Request, *args, **kwargs):
        print("Atendiendo preguntas")
        data = JSONParser().parse(request)
        serializer = serializer.ChatSerializer(data=data)
        if serializer.is_valid():
            ask_message = serializer.data.get("message")
            chat = Chat(list(Intent.objects.values()))
            message = chat.begin(ask_message)
            return Response({'message':message, 'userType':'AGENT'})
        return response({'message':'SIN RESPUESTA', 'userType':'AGENT'})