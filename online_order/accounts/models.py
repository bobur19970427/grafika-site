from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    manzil = models.CharField(max_length=250, blank=True, null=True)
    tel = models.CharField(max_length=20, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)