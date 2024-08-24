from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, View
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import JsonResponse

from .models import Cart, CartItem
from menu.models import Dish
from user.models import UserAddress
from orders.models import Order, OrderItem


class CartView(LoginRequiredMixin, TemplateView):
    template_name = 'cart/cart_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart.objects.filter(
            user=self.request.user, delivery_address=None).first()
        addresses = UserAddress.objects.filter(user=self.request.user)
        context['cart'] = cart
        context['addresses'] = addresses
        return context


class AddToCartView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        dish_id = request.POST.get('dish_id')
        quantity = request.POST.get('quantity', '1')

        quantity = int(quantity)
        dish = get_object_or_404(Dish, id=dish_id)

        if dish.availability != "available":
            messages.error(
                request, "This dish is not available and cannot be added to the cart.")
            return redirect('menu:dish_list_by_category', category=dish.category)

        cart, created = Cart.objects.get_or_create(
            user=request.user, delivery_address=None)

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart, dish=dish)
        cart_item.quantity += quantity
        cart_item.save()

        cart.cost = sum(item.get_total_price() for item in cart.items.all())
        cart.save()

        return redirect('menu:dish_list_by_category', category=dish.category)


class RemoveFromCartView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        item_id = request.POST.get('item_id')

        cart_item = get_object_or_404(
            CartItem, id=item_id, cart__user=request.user)
        cart = cart_item.cart

        cart_item.delete()

        cart.cost = sum(item.get_total_price() for item in cart.items.all())
        cart.save()

        return redirect('cart-detail')


class UpdateCartItemQuantityView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        item_id = request.POST.get('item_id')
        quantity_change = request.POST.get('quantity_change')

        if quantity_change:
            quantity_change = int(quantity_change)
            cart_item = get_object_or_404(
                CartItem, id=item_id, cart__user=request.user)
            new_quantity = max(cart_item.quantity + quantity_change, 1)
            cart_item.quantity = new_quantity
            cart_item.save()

            cart = cart_item.cart
            cart.cost = sum(item.get_total_price()
                            for item in cart.items.all())
            cart.save()

        return redirect('cart-detail')


class UpdateAddressView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        address_id = request.POST.get('address')
        request.session['selected_address'] = address_id
        return JsonResponse({'selected_address': address_id})


class OrderConfirmationView(View):
    def post(self, request, *args, **kwargs):
        cart = Cart.objects.filter(
            user=request.user, delivery_address=None).first()

        selected_address_id = request.session.get('selected_address')

        if not selected_address_id:
            return redirect('cart-detail')

        if cart:
            order = self.save_order_from_cart(cart, selected_address_id)

            cart.items.all().delete()
            cart.delete()

        return redirect(reverse_lazy('confirm-order'))

    def get(self, request, *args, **kwargs):
        return self.render_to_response({})

    def render_to_response(self, context, **response_kwargs):
        return render(self.request, 'cart/order_confirm.html', context, **response_kwargs)

    def save_order_from_cart(self, cart, address_id):
        order = Order.objects.create(
            user=cart.user,
            delivery_address=UserAddress.objects.get(id=address_id),
            cost=cart.cost,
        )
        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                dish=item.dish,
                quantity=item.quantity,
            )
        order.is_completed = True
        order.save()
        return order
