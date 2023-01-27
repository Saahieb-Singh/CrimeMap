from django.db import models

# Create your models here.

# class Report(models.Model):
#     reportid=models.IntegerField(primary_key=True)
#     case_type=models.CharField(max_length=40)
#     loc=models.CharField(max_length=80)
#     pincode=models.IntegerField()
#     case_details=models.CharField(max_length=200)
#     date=models.DateField(auto_now=False, auto_now_add=True)
#     time=models.TimeField(auto_now=False, auto_now_add=True)

class Report(models.Model):
    Fir_Id=models.IntegerField(primary_key=True)
    Dhaara=models.CharField(max_length=50)
    Police_St_ID=models.IntegerField()
    Location=models.CharField(max_length=80)
    Case_Details=models.CharField(max_length=200)
    Date_Time=models.DateTimeField(auto_now=False, auto_now_add=False)
    longitute=models.DecimalField(max_digits=15, decimal_places=10)
    latitude=models.DecimalField(max_digits=15, decimal_places=10)
    

    
