from django.urls import path
from orders.views import OrdersView
from user.views import ProfileView, AddressesView, AddAddressView, EditAddressView, DeleteAddressView

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('orders/', OrdersView.as_view(), name='orders'),
    path('addresses/', AddressesView.as_view(), name='user-addresses'),
    path('addresses/add/', AddAddressView.as_view(), name='add-address'),
    path('addresses/edit/<int:pk>/',
         EditAddressView.as_view(), name='edit-address'),
    path('addresses/delete/<int:pk>/',
         DeleteAddressView.as_view(), name='delete-address'),
]
