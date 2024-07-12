from django.views.generic import ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Dish

class AppetizerListView(ListView):
    model = Dish
    template_name = 'menu/appetizer_list.html'
    context_object_name = 'dishes'

    def get_queryset(self):
        return Dish.objects.filter(category='appetizer')

class DishUpdateView(UpdateView):
    model = Dish
    template_name = 'menu/dish_update.html'
    fields = ['name', 'description', 'availability', 'price', 'photo']
    success_url = reverse_lazy('menu:appetizer-list')

class DishDeleteView(DeleteView):
    model = Dish
    template_name = 'menu/dish_confirm_delete.html'
    success_url = reverse_lazy('menu:appetizer-list')
