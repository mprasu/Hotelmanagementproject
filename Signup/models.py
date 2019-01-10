from django.db import models
from django import forms

# Create your models here.
class SignupModel(models.Model):
	Name=models.CharField(max_length=50)
	Age=models.IntegerField()
	Email_id=models.EmailField(max_length=80,unique=True)
	Password=models.CharField(max_length=20)
	ConfirmPassword=models.CharField(max_length=20)
	Phonenumber=models.IntegerField()
	Location=models.CharField(max_length=50)
	State=models.CharField(max_length=50)
	Country=models.CharField(max_length=50)
	Address=models.CharField(max_length=50)
	Image = models.ImageField(upload_to='profile_image', blank=True)
	
	def __str__(self):
		return self.Name
