from django.urls import path
from . import views

urlpatterns=[
      path('',views.customer_home,name='customer_home'),
      path('registration_page',views.registration_page,name='registration_page'),
      path('login_page',views.login_page,name='login_page'),
      path('register',views.register,name='register'),
      path('login',views.user_login,name='login'),
      path('profile',views.profile_page,name='profile_page'),
      path('logout',views.user_logout,name='logout'),
      path('cart_page',views.cart_page,name='cart_page')
]