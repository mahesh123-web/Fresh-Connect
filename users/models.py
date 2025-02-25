from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class farmerprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)  # Link to User model

    name = models.CharField(max_length=100)
    farm_location = models.CharField(max_length=200)
    farm_size = models.FloatField()
    crops_produced = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Store hashed passwords


    def __str__(self):
        return self.name

class Customerprofile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)  # Link to User model
    name = models.CharField(max_length=100)
    delivery_address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Store hashed passwords

    def __str__(self):
        return self.name
