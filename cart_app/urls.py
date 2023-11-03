from django.urls import path
from .import views


urlpatterns=[
      path('',views.cart_page,name='cart'),
      path('add_to_cart/<int:i>',views.add_to_cart,name='add_to_cart')
]