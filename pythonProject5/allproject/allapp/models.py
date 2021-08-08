from django.db import models

# Create your models here.
class student(models.Model):
    stuid=models.IntegerField(primary_key=True)
    stuname=models.CharField(max_length=20)
    stuemail=models.EmailField(max_length=40)
    stupass=models.CharField(max_length=40)
    stumarks=models.IntegerField(null=True)
    stuavg=models.IntegerField(default=True)
    stupercent=models.IntegerField(blank=True)


class AlterModelTable(student):
    class Meta:
        db_table = 'empname'