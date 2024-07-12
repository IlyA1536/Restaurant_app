from django.urls import path
from main.views import MainPageView, DishCreateView

urlpatterns = [
    path('', MainPageView.as_view(), name='main-page'),
    path('add-dish/', DishCreateView.as_view(), name='add-dish'),
]

app_name = 'main'
