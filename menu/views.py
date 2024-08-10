from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Dish, Review

class AppetizersListView(ListView):
    model = Dish
    template_name = 'menu/appetizers_list.html'
    context_object_name = 'dishes'

    def get_queryset(self):
        return Dish.objects.filter(category='appetizers')


class SaladsListView(ListView):
    model = Dish
    template_name = 'menu/salads_list.html'
    context_object_name = 'dishes'

    def get_queryset(self):
        return Dish.objects.filter(category='salads')


class SoupsListView(ListView):
    model = Dish
    template_name = 'menu/soups_list.html'
    context_object_name = 'dishes'

    def get_queryset(self):
        return Dish.objects.filter(category='soups')


class SideDishesListView(ListView):
    model = Dish
    template_name = 'menu/side_dishes_list.html'
    context_object_name = 'dishes'

    def get_queryset(self):
        return Dish.objects.filter(category='sidedishes')


class DessertsListView(ListView):
    model = Dish
    template_name = 'menu/desserts_list.html'
    context_object_name = 'dishes'

    def get_queryset(self):
        return Dish.objects.filter(category='desserts')


class SoftDrinksListView(ListView):
    model = Dish
    template_name = 'menu/soft_drinks_list.html'
    context_object_name = 'dishes'

    def get_queryset(self):
        return Dish.objects.filter(category='softdrinks')


class AlcoholListView(ListView):
    model = Dish
    template_name = 'menu/alcohol_list.html'
    context_object_name = 'dishes'

    def get_queryset(self):
        return Dish.objects.filter(category='alcohol')

class DishUpdateView(UpdateView):
    model = Dish
    template_name = 'menu/dish_update.html'
    fields = ['name', 'description', 'availability', 'price', 'photo']
    success_url = reverse_lazy('main:main-page')

class DishDeleteView(DeleteView):
    model = Dish

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER')


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
        return reverse_lazy('main:main-page')


class ReviewDeleteView(DeleteView):
    model = Review

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER')
