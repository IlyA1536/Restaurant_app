from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from menu.models import Dish

class MainPageView(TemplateView):
    template_name = 'main/main_page.html'

def home(request):
    if request.user.is_authenticated:
        avatar_url = request.user.avatar.url if request.user.avatar else None
    else:
        avatar_url = None

    return render(request, 'main/main_page.html', {'avatar_url': avatar_url})


class DishCreateView(CreateView):
    model = Dish
    template_name = 'main/dish_form.html'
    fields = ['name', 'description', 'category','availability', 'price', 'image']

    def get_success_url(self):
        return reverse_lazy('main:main-page')
