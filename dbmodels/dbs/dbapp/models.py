from django.db import models

# Create your models here.
class Data(models.Model):
    name = models.EmailField(max_length=70)
    password = models.CharField(max_length=70)
