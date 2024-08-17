from django.urls import path
from .views import profile_view, addresses_view, add_address_view, edit_address_view, delete_address_view

urlpatterns = [
    path('user/profile/', profile_view, name='profile'),
    path('user/addresses/', addresses_view, name='addresses'),
    path('user/addresses/add/', add_address_view, name='add-address'),
    path('user/addresses/edit/<int:pk>/', edit_address_view, name='edit-address'),
    path('user/addresses/delete/<int:pk>/', delete_address_view, name='delete-address'),
]
