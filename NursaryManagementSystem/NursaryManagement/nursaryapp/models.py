from django.db import models

# Create your models here.
class User(models.Model):
    batch = models.IntegerField(null=True)
    name = models.CharField(max_length=100,null=True)
    type = models.CharField(max_length=100,null=True)
    details = models.CharField(max_length=100,null=True)
    Seeds = models.CharField(max_length=100,null=True)
    quantity = models.IntegerField(null=True)