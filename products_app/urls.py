from django.urls import path
from . import views

urlpatterns=[
      path('products_page',views.products_page,name='products_page'),
      path('add_category',views.add_category,name='add_category'),
      path('add_product',views.add_product,name='add_product'),
      path('delete_product/<int:p>',views.delete_product,name='delete_product'),
      path('edit_product_page/<int:p>',views.edit_product_page,name='edit_product_page')
]