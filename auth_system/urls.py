from django.urls import path
from .views import RegisterView, CustomLogoutView, CustomLoginView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]

app_name = 'auth_system'
