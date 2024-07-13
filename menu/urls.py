from django.urls import path
from .views import AppetizersListView, SaladsListView, DishUpdateView, DishDeleteView, ReviewCreateView, ReviewDeleteView

urlpatterns = [
    path('appetizers/', AppetizersListView.as_view(), name='appetizers-list'),
    path('salads/', SaladsListView.as_view(), name='salads-list'),
    path('update/<int:pk>/', DishUpdateView.as_view(), name='update-dish'),
    path('delete/<int:pk>/', DishDeleteView.as_view(), name='delete-dish'),
    path('review/<int:pk>/', ReviewCreateView.as_view(), name='add-review'),
    path('review/<int:pk>/delete/', ReviewDeleteView.as_view(), name='delete-review'),
]

app_name = 'menu'
