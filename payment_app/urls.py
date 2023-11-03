from django.urls import path
from .import views

urlpatterns=[
      path('pay_order',views.pay_order,name='pay_order'),
      # path('payment_status',views.payment_status,name='payment_status')
]