from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.http import JsonResponse
from django.shortcuts import redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from .models import Order
from cart.models import Cart, CartItem


class OrdersView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'user/orders.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-created_at')


class RepeatOrderView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        order = get_object_or_404(Order, pk=kwargs['pk'], user=request.user)
        cart, created = Cart.objects.get_or_create(
            user=request.user, delivery_address=None)
        cart.items.all().delete()

        for item in order.items.all():
            CartItem.objects.create(
                cart=cart,
                dish=item.dish,
                quantity=item.quantity
            )

        cart.cost = sum(item.get_total_price() for item in cart.items.all())
        cart.save()

        return redirect('cart-detail')


class OrderDetailsAjaxView(View):
    def get(self, request, *args, **kwargs):
        order_id = request.GET.get('order_id')
        try:
            order = Order.objects.get(id=order_id, user=request.user)
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Order not found'}, status=404)

        items = [
            {
                'name': str(item.dish.name),
                'quantity': item.quantity,
                'total_price': item.get_total_price(),
                'image_url': item.dish.image.url if item.dish.image else None
            }
            for item in order.items.all()
        ]

        return JsonResponse({'items': items})
