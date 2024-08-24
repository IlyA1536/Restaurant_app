from django.views.generic import TemplateView
from django.views.generic import CreateView, FormView, ListView, DeleteView
from django.urls import reverse_lazy
from menu.models import Dish
from .forms import ManageRecommendedDishesForm
from .models import CarouselImage


class MainPageView(TemplateView):
    template_name = 'main/main_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recommended_dishes'] = Dish.objects.filter(
            is_recommended=True)
        context['carousel_images'] = CarouselImage.objects.all()
        return context


class DishCreateView(CreateView):
    model = Dish
    template_name = 'main/dish_form.html'
    fields = ['name', 'description', 'category',
              'availability', 'price', 'image']

    def get_success_url(self):
        return reverse_lazy('main:main-page')


class ManageRecommendedDishesView(FormView):
    template_name = 'main/manage_recommended_dishes.html'
    form_class = ManageRecommendedDishesForm
    success_url = reverse_lazy('main:main-page')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['initial'] = Dish.objects.filter(is_recommended=True)
        return kwargs

    def form_valid(self, form):
        dish_ids = form.cleaned_data['recommended_dishes']
        Dish.objects.update(is_recommended=False)
        Dish.objects.filter(id__in=dish_ids).update(is_recommended=True)
        return super().form_valid(form)


class CarouselImageListView(ListView):
    model = CarouselImage
    template_name = 'main/manage_carousel.html'
    context_object_name = 'carousel_images'


class CarouselImageCreateView(CreateView):
    model = CarouselImage
    fields = ['image']
    success_url = reverse_lazy('main:manage_carousel')


class CarouselImageDeleteView(DeleteView):
    model = CarouselImage
    success_url = reverse_lazy('main:manage_carousel')
