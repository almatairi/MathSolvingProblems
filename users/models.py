from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE ,  null=True , blank=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)

    def __str__(self):
        return self.username