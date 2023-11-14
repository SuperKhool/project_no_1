from django.urls import path
from .views import product ,add_to_cart
urlpatterns = [
    path('product/',product,name='product'),
    path('add_to_cart/<int:id>/',add_to_cart,name='add_to_cart')
   
]
