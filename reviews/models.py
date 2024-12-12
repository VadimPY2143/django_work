from django.db import models
from base import TimeStamp
from products.models import Products
from users.models import User


class Review(TimeStamp):
    comment = models.TextField()
    rating = models.PositiveIntegerField()
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)