from django.db import models

# Create your models here.
class Data(models.Model):
    name=models.CharField(max_length=40)
    mail=models.EmailField(max_length=30)
    message=models.TextField(max_length=500)


