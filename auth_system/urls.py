from django.urls import path
from django.urls import reverse_lazy
from .views import RegisterView, CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('main:main-page')), name='logout'),
]

app_name = 'auth_system'
