
from chat.models import Intent
from rest_framework import viewsets
from chat.serializer import IntentSerializer
# Create your views here.
class IntentViewSet(viewsets.ModelViewSet):
    queryset = Intent.objects.all()
    serializer_class = IntentSerializer