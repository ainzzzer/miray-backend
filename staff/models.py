from django.db import models
from django.contrib.auth.models import User


class Staff(models.Model):
    account = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="staff")
    fullname = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=18, unique=True)
    password = models.CharField(max_length=150)
