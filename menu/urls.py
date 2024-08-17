from django.urls import path
from .views import DishUpdateView, DishDeleteView, ReviewCreateView, ReviewDeleteView, DishListView

urlpatterns = [
    path('<str:category>/', DishListView.as_view(), name='dish_list_by_category'),
    path('update/<int:pk>/', DishUpdateView.as_view(), name='update-dish'),
    path('delete/<int:pk>/', DishDeleteView.as_view(), name='delete-dish'),
    path('review/<int:pk>/', ReviewCreateView.as_view(), name='add-review'),
    path('review/<int:pk>/delete/', ReviewDeleteView.as_view(), name='delete-review'),
]

app_name = 'menu'
