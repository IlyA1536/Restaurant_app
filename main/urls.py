from django.urls import path
from main.views import MainPageView, DishCreateView, ManageRecommendedDishesView

urlpatterns = [
    path('', MainPageView.as_view(), name='main-page'),
    path('add-dish/', DishCreateView.as_view(), name='add-dish'),
    path('manage-recommended-dishes/', ManageRecommendedDishesView.as_view(), name='manage_recommended_dishes'),
]

app_name = 'main'
