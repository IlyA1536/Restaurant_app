from django.urls import path
from user.views import ProfileView, AddressesView, AddAddressView, EditAddressView, DeleteAddressView

urlpatterns = [
    path('user/profile/', ProfileView.as_view(), name='profile'),
    path('user/addresses/', AddressesView.as_view(), name='user-addresses'),
    path('user/addresses/add/', AddAddressView.as_view(), name='add-address'),
    path('user/addresses/edit/<int:pk>/', EditAddressView.as_view(), name='edit-address'),
    path('user/addresses/delete/<int:pk>/', DeleteAddressView.as_view(), name='delete-address'),
]
