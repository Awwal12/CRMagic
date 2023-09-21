from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.


class Record(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    zipcode = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (f'{self.first_name} {self.last_name}')
