from django.db import models

from Difficulty.models import Difficulty


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField
    difficulty = models.OneToOneField(Difficulty, on_delete=models.CASCADE)

    def __str__(self):
        return self.title