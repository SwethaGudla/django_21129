from crudapp.managers import CustomManager
from django.db import models
from .managers import CustomManager

# Create your models here.
class StudentRegistration(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    phone = models.IntegerField()
    email = models.EmailField(max_length=60)
    branch = models.CharField(max_length=60)
    address = models.TextField()

    student = CustomManager()

