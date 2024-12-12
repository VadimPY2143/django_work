from django.db import models

from base import TimeStamp
from orders.models import Order


class Payment(TimeStamp):
    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("COMPLETED", "Completed"),
        ("FAILED", "Failed"),
    ]

    PAYMENT_TYPES = [
        ('CREDIT_CARD', 'Credit Card'),
        ('PAYPAL', 'Paypal'),
        ('BANK_TRANSFER', 'Bank Transfer')
    ]

    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=20, choices=PAYMENT_TYPES, default='PAYPAL')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
