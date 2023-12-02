from django.db import models

from difficulty.models import Difficulty


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255,null=False , blank=False)
    # description can be empty
    description = models.TextField(null=True , blank=True)
    difficulty = models.ForeignKey(Difficulty, on_delete=models.CASCADE,null=False , blank=False)

    def __str__(self):
        return self.title