from django.db import models

# Create your models here.

class Students(models.Model):
    roll_no=models.IntegerField()
    name=models.CharField(max_length=100)
    cource=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    phone_no=models.IntegerField()
