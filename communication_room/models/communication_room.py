from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class CommunicationRoom(models.Model):
    room_name = models.CharField(max_length=255)
    allow_users = models.CharField(max_length=255)
