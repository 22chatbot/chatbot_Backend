from django.shortcuts import render
from chat.models import Intenciones
from rest_framework import viewsets
from chat.serializer import IntencionesSerializer
# Create your views here.
class IntencionesViewset(viewsets.ModelViewSet):
    queryset = Intenciones.objects.all()
    serializer_class = IntencionesSerializer