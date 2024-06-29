from django.db import models
from user.models import CustomUser

class Restaurant(models.Model):
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f"{self.city} {self.address}"

class Dish(models.Model):
    CATEGORY_CHOICES = (
        ('appetizer', 'Appetizer'),
        ('salads', 'Salads'),
        ('soups', 'Soups'),
        ('sidedishes', 'Side dishes'),
        ('desserts', 'Desserts'),
        ('softdrinks', 'Soft drinks'),
        ('alcohol', 'Alcohol'),
    )

    AVAILABILITY_CHOICES = (
        ('instock', 'In stock'),
        ('notavailable', 'Not available'),
    )

    restaurants = models.ManyToManyField(Restaurant, through='RestaurantDish')
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    category = models.CharField(max_length=31, choices=CATEGORY_CHOICES, null=False, blank=False)

    def __str__(self):
        return self.name


class RestaurantDish(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    availability = models.CharField(max_length=31, choices=Dish.AVAILABILITY_CHOICES, default='instock')

    def __str__(self):
        return f"{self.dish} in {self.restaurant}: {self.price} UAH. (Availability: {self.get_availability_display()})"

    class Meta:
        unique_together = ('restaurant', 'dish')


class Review(models.Model):
    RATING_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rating = models.CharField(max_length=1, choices=RATING_CHOICES)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback on {self.restaurant} {self.dish} by {self.author}: {self.rating}/5 - {self.text[:50]}"
