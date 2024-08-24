from django.contrib import admin
from .models import Dish, Review


class DishAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_display = ('description',)
    search_fields = ('description',)


admin.site.register(Dish)
admin.site.register(Review)
