from django.urls import path
from .views import RepeatOrderView, OrderDetailsAjaxView

urlpatterns = [
    path('<int:pk>/repeat/', RepeatOrderView.as_view(), name='repeat-order'),
    path('details-ajax/', OrderDetailsAjaxView.as_view(), name='order-details-ajax'),
]
