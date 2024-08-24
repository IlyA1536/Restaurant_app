from django.urls import path
from main.views import MainPageView, DishCreateView, ManageRecommendedDishesView, CarouselImageListView, CarouselImageCreateView, CarouselImageDeleteView

urlpatterns = [
    path('', MainPageView.as_view(), name='main-page'),
    path('add-dish/', DishCreateView.as_view(), name='add-dish'),
    path('manage-recommended-dishes/', ManageRecommendedDishesView.as_view(),
         name='manage_recommended_dishes'),
    path('manage-carousel/', CarouselImageListView.as_view(), name='manage_carousel'),
    path('add-carousel-image/', CarouselImageCreateView.as_view(),
         name='add_carousel_image'),
    path('delete-carousel-image/<int:pk>/',
         CarouselImageDeleteView.as_view(), name='delete_carousel_image'),
]

app_name = 'main'
