from django import forms
from .models import CartItem, Cart


class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['quantity']


class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['delivery_address']
