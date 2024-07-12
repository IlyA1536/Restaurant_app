from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Dish, Review

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


class ReviewCreateView(CreateView):
    model = Review
    template_name = 'menu/review_form.html'
    fields = ['rating', 'comment']

    def form_valid(self, form):
        form.instance.author = self.request.user
        dish = Dish.objects.get(pk=self.kwargs['pk'])
        form.instance.dish = dish
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dish = Dish.objects.get(pk=self.kwargs['pk'])
        context['dish_name'] = dish.name
        return context

    def get_success_url(self):
        return reverse_lazy('menu:appetizer-list')


class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'menu/review_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('menu:appetizer-list')
