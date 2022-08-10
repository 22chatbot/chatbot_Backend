from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from chat.views import IntencionesViewset

router = DefaultRouter()
router.register('/api/intenciones', IntencionesViewset, basename='intenciones')

urlpatterns = [
]
urlpatterns += router.urls