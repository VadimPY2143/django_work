from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=255, null=False)
    date = models.DateTimeField(auto_now_add=True)

