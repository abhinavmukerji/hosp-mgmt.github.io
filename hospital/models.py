from django.db import models
from django.core.validators import MaxValueValidator
# Create your models here.

class Doctor(models.Model):
	Name=models.CharField(max_length=50)
	mobile=models.IntegerField(unique=True)
	special=models.CharField(max_length=50)
class Patient(models.Model):
	name=models.CharField(max_length=50)
	gender=models.CharField(max_length=10)
	mobile=models.IntegerField(null=True,unique=True)
	address=models.TextField()
class Appointment(models.Model):
	Doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
	Patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
	date=models.DateField()
	time=models.TimeField()


#by Abhinav Mukerji(EN18CS301006)
	
