from django.db import models
from user.models import CustomUser, UserAddress
from menu.models import Dish


class Order(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='orders')
    delivery_address = models.ForeignKey(
        UserAddress, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Order of {self.user.username}'

    def get_total_price(self):
        total_items_price = sum(item.get_total_price()
                                for item in self.items.all())
        return total_items_price + self.cost

    def get_items_count(self):
        return self.items.count()


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='items')
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.quantity} x {self.dish.name}'

    def get_total_price(self):
        return self.quantity * self.dish.price
