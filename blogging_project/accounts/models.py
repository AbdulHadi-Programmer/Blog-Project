from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    fullname = models.CharField(max_length=180, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)



