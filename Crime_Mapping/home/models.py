from django.db import models

# Create your models here.

class Report(models.Model):
    reportid=models.IntegerField(primary_key=True)
    case_type=models.CharField(max_length=40)
    loc=models.CharField(max_length=80)
    pincode=models.IntegerField()
    case_details=models.CharField(max_length=200)
    date=models.DateField(auto_now=False, auto_now_add=True)
    time=models.TimeField(auto_now=False, auto_now_add=True)

    

    
