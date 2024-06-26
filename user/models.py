from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'Not specified'),
    )

    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    address = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='N')
    date_of_birth = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='user-avatars/',  blank=True, null=False, default='static/img/default.jpg')

    def __str__(self):
        return self.username
