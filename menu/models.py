from django.db import models
from django.core.validators import MinValueValidator
from django.db.models import Avg
from user.models import CustomUser


class Dish(models.Model):
    CATEGORY_CHOICES = (
        ('appetizers', 'Appetizers'),
        ('salads', 'Salads'),
        ('soups', 'Soups'),
        ('sidedishes', 'Side dishes'),
        ('desserts', 'Desserts'),
        ('softdrinks', 'Soft drinks'),
        ('alcohol', 'Alcohol'),
    )

    AVAILABILITY_CHOICES = (
        ('available', 'Available'),
        ('notavailable', 'Not available'),
    )

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    category = models.CharField(max_length=31, choices=CATEGORY_CHOICES, null=False, blank=False)
    price = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0, message="The price cannot be negative.")])
    availability = models.CharField(max_length=31, choices=AVAILABILITY_CHOICES, default='available')
    image = models.ImageField(upload_to='dishes/', null=False, blank=True)

    def average_rating(self):
        average = self.review_set.aggregate(Avg('rating'))['rating__avg'] or 0
        return round(average, 1)

    def __str__(self):
        return self.name


class Review(models.Model):
    RATING_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )

    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rating = models.CharField(max_length=1, choices=RATING_CHOICES)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback on {self.dish} by {self.author}: {self.rating}/5 - {self.text[:50]}"
