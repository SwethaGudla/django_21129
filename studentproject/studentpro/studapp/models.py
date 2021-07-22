from django.db import models


# Create your models here.
class Student(models.Model):
    stdid=models.CharField(max_length=70)
    stdemail=models.EmailField(max_length=70)
    password=models.CharField(max_length=70)

