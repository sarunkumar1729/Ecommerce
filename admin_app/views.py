from django.shortcuts import render
from customer_app.models import customer_model

# Create your views here.

def admin_home(request):
      return render(request,'admin/admin_home.html')

def user_details(request):
      users=customer_model.objects.all()
      return render(request,'admin/users.html',{'users':users})