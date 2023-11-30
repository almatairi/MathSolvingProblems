from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username
class Posts(models.Model):
    name = models.CharField(max_length=255)
    difficulty = models.CharField(max_length=255)

    def __str__(self):
        return self.name
class Difficulty(models.Model):
    title = models.CharField(max_length=255)