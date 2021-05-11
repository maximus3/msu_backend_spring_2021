from django.db import models
from chats.models import Chat

class User(models.Model):
    username = models.CharField(max_length=32, verbose_name='Username')
    chats = models.ManyToManyField(Chat)
