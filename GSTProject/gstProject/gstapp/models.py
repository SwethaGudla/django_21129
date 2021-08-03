from django.db import models


# Create your models here.
class GstRegistration(models.Model):
    Invoice_Number = models.IntegerField(primary_key=True)
    Date = models.DateTimeField()
    Customer_Name = models.CharField(max_length=50)
    Customer_Address = models.CharField(max_length=50)
    Customer_Mobile_Number = models.IntegerField()
    Product = models.CharField(max_length=70)
    Product_Price = models.IntegerField()
    GST = models.IntegerField()
    Total = models.IntegerField()
