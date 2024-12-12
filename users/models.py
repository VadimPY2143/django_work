from django.db import models
from base import TimeStamp

class User(TimeStamp):
    full_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)