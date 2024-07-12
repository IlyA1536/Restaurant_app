from django.urls import path
from .views import AppetizerListView, DishUpdateView, DishDeleteView

urlpatterns = [
    path('appetizers/', AppetizerListView.as_view(), name='appetizer-list'),
    path('update/<int:pk>/', DishUpdateView.as_view(), name='update_dish'),
    path('delete/<int:pk>/', DishDeleteView.as_view(), name='delete_dish'),
]

app_name = 'menu'
