from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from products_app.models import product
from .models import cart,cart_item
# Create your views here.

def cart_page(request):
      current_user=request.user
      crt=cart.objects.get(user=current_user)
      cart_items=crt.items.all()
      total=0
      for c in cart_items:
            total=total+((c.quantity)*(c.item.price))
      return render(request,'customer/cart.html',{'cart_items':cart_items,'total':total})

def add_to_cart(request,i):
      current_user=request.user
      item=product.objects.get(id=i)
      qty=1
      price=item.price
      try:
            user_cart=cart.objects.get(user=current_user)
            new_cart_item=cart_item(item=item,quantity=qty,price=price)
            new_cart_item.save()
            user_cart.items.add(new_cart_item)
            user_cart.save()
      except:
            user_cart=cart(user=current_user)
            user_cart.save()
            new_cart_item=cart_item(item=item,quantity=qty,price=price)
            new_cart_item.save()
            user_cart.items.add(new_cart_item)
            user_cart.save()
      return redirect('cart')


