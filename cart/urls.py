from django.urls import path
from .views import CartView, AddToCartView, RemoveFromCartView, UpdateCartItemQuantityView, UpdateAddressView, OrderConfirmationView

urlpatterns = [
    path('detail/', CartView.as_view(), name='cart-detail'),
    path('add-item/', AddToCartView.as_view(), name='cart-add-item'),
    path('remove-item/', RemoveFromCartView.as_view(), name='cart-remove-item'),
    path('update/', UpdateCartItemQuantityView.as_view(), name='cart-update-quantity'),
    path('update-address/', UpdateAddressView.as_view(), name='update-address'),
    path('confirm-order/', OrderConfirmationView.as_view(), name='confirm-order'),
]
