from django.db import models

# Create your models here.
class AoK(models.Model):
    actor = models.CharField(max_length=100)
    recipient = models.CharField(max_length=100)
    act = models.CharField(max_length=200)

