from django.contrib import admin
from .models import *

admin.site.register(Restaurant)
admin.site.register(Dish)
admin.site.register(RestaurantDish)
admin.site.register(Review)
