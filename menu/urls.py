from django.urls import path
from .views import AppetizersListView, SaladsListView, SoupsListView, SideDishesListView, DessertsListView, SoftDrinksListView, AlcoholListView, DishUpdateView, DishDeleteView, ReviewCreateView, ReviewDeleteView

urlpatterns = [
    path('appetizers/', AppetizersListView.as_view(), name='appetizers-list'),
    path('salads/', SaladsListView.as_view(), name='salads-list'),
    path('soups/', SoupsListView.as_view(), name='soups-list'),
    path('side-dishes/', SideDishesListView.as_view(), name='side-dishes-list'),
    path('desserts/', DessertsListView.as_view(), name='desserts-list'),
    path('soft-drinks/', SoftDrinksListView.as_view(), name='soft-drinks-list'),
    path('alcohol/', AlcoholListView.as_view(), name='alcohol-list'),
    path('update/<int:pk>/', DishUpdateView.as_view(), name='update-dish'),
    path('delete/<int:pk>/', DishDeleteView.as_view(), name='delete-dish'),
    path('review/<int:pk>/', ReviewCreateView.as_view(), name='add-review'),
    path('review/<int:pk>/delete/', ReviewDeleteView.as_view(), name='delete-review'),
]

app_name = 'menu'
