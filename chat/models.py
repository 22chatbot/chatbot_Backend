
from email import message
from http.client import responses
from multiprocessing import context
from django.db import models
from django. contrib.postgres.fields import ArrayField
# Create your models here.

class Intent (models.Model):
    tag = models.CharField(max_length=60)
    patterns = ArrayField(models.CharField(max_length=255), default=list, blank=True)
    responses = ArrayField(models.CharField(max_length=255), default=list, blank=True)
    context = ArrayField(models.CharField(max_length=255), default=list, blank=True)

class Chat(models.Model):
    message = models.CharField(max_length=255)
    userType = models.CharField(max_length=10)