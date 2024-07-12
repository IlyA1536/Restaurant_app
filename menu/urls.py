from django.urls import path
from .views import AppetizerListView, DishUpdateView, DishDeleteView, ReviewCreateView, ReviewDeleteView

urlpatterns = [
    path('appetizers/', AppetizerListView.as_view(), name='appetizer-list'),
    path('update/<int:pk>/', DishUpdateView.as_view(), name='update-dish'),
    path('delete/<int:pk>/', DishDeleteView.as_view(), name='delete-dish'),
    path('review/<int:pk>/', ReviewCreateView.as_view(), name='add-review'),
    path('review/<int:pk>/delete/', ReviewDeleteView.as_view(), name='delete-review'),
]

app_name = 'menu'
