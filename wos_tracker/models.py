from django.db import models


class Client(models.Model):
    name = models.CharField(null=False, max_length=100)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    updated_on = models.DateTimeField(auto_now=True)

