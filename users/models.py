from django.db import models
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=225, unique=True)
    password = models.CharField(max_length=225)  # Store the hashed password
    is_active = models.BooleanField(default=True)


    def set_password(self, raw_password):
        validate_password(raw_password)  # Ensure password meets security standards
        self.password = make_password(raw_password)