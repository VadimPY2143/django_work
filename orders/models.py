from django.db import models
from base import TimeStamp
from users.models import User


class Order(TimeStamp):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled')
    ]


    status = models.CharField(choices=STATUS_CHOICES, default='PENDING', max_length=50)
    total_price = models.DecimalField(decimal_places=2, max_digits=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')