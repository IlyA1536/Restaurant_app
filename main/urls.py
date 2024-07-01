from django.contrib import admin
from django.urls import path
from main.views import MainPageView

urlpatterns = [
    path('', MainPageView.as_view(), name='main-page'),
]

app_name = 'main'
