from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    account = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="client")
    fullname = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=18, unique=True)
    password = models.CharField(max_length=150)
    has_permission = models.BooleanField(default=False)
    expire_date = models.DateField(null=True, blank=True)
