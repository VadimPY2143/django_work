from django.db import models

from base import TimeStamp
from orders.models import Order
from users.models import User


class ShippingAddress(TimeStamp):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50)