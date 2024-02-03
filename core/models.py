from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime
User=get_user_model()
# Create your models here.
class Profile(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    id_user=models.IntegerField()
    profileimg=models.ImageField(upload_to='profile_images',default="user.png")

    def __str__(self):
        return self.user.username

    def delete_user(self):
        self.user.delete()

class Image(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='images/')
    upload_at=models.DateTimeField(default=datetime.now)
    description=models.TextField(default='')
 
class Patient(models.Model):
    name = models.CharField(max_length=100)

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_date = models.DateField()