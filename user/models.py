from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    avatar = models.ImageField(
        upload_to='user_avatars/', blank=True, null=True)

    def __str__(self):
        return self.username


class UserAddress(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='addresses')
    city = models.CharField(max_length=63)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=10)
    entrance_number = models.CharField(max_length=10, blank=True)
    floor_number = models.CharField(max_length=10, blank=True)
    apartment_number = models.CharField(max_length=10, blank=True)
    comment = models.TextField(blank=True)

    def __str__(self):
        return f"{self.city}, {self.street}, {self.house_number}"
