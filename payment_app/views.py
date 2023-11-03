from django.shortcuts import render,redirect
from .models import payment
import razorpay
from cart_app.models import cart_item,cart

# Create your views here.

def pay_order(request):
      if request.method=='POST':
            name=request.POST.get('name')
            a=request.POST.get('amount')
            amount=int(a)*100
            print(type(amount))
            print(name)
            print(amount)
            #create razorpay client
            client=razorpay.Client(auth=('rzp_test_y6QiMSkcMNKsTw','UgFuvjxdgzqg4Uo3AOGu1Ngz'))
            #create order
            response_payment=client.order.create(dict(amount=amount,currency='INR'))
            order_id=response_payment['id']
            order_status=response_payment['status']
            if order_status=='created':
                  # c=cofee(
                  #       name=name,
                  #       amount=amount,
                  #       order_id=order_id
                  # )
                  # c.save()
                  response_payment['name']=name
                  print(response_payment)
                  return render(request,'customer/cart.html',{'payment':response_payment})
      else:
            return render(request,'customer/cart.html')