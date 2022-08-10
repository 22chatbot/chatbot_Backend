from django.db import models

# Create your models here.

class Intenciones (models.Model):
    tag = models.CharField(max_length=60)