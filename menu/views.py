from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Dish, Review


class DishListView(ListView):
    model = Dish
    template_name = 'menu/dish_list.html'
    context_object_name = 'dishes'

    def get_queryset(self):
        self.category = self.kwargs['category']
        return Dish.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = dict(Dish.CATEGORY_CHOICES).get(self.category, self.category)
        return context


class DishUpdateView(UpdateView):
    model = Dish
    template_name = 'menu/dish_update.html'
    fields = ['name', 'description', 'availability', 'price', 'image']

    def get_success_url(self):
        category = self.object.category
        return reverse_lazy('menu:dish_list_by_category', kwargs={'category': category})

class DishDeleteView(DeleteView):
    model = Dish

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER')


class ReviewCreateView(CreateView):
    model = Review
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
        return self.request.META.get('HTTP_REFERER')


class ReviewDeleteView(DeleteView):
    model = Review

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER')
