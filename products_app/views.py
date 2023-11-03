from django.shortcuts import render,redirect
from .models import category,product

# Create your views here.

def products_page(request):
      categories=category.objects.all()
      products=product.objects.all()
      return render(request,'admin/product.html',{'cat':categories,'product':products})

def add_category(request):
      if request.method=='POST':
            category_name=request.POST['category']
            new_category=category(name=category_name)
            new_category.save()
            print('success')
            return redirect('products_page')

def add_product(request):
      if request.method=='POST':
            product_name=request.POST['name']
            product_description=request.POST['description']
            product_category_id=request.POST['category']
            product_category=category.objects.get(id=product_category_id)
            product_price=request.POST['price']
            product_count=request.POST['count']
            product_photo=request.FILES.get('photo')
            new_product=product(name=product_name,category=product_category,description=product_description,price=product_price,count=product_count,photo=product_photo)
            new_product.save()
            print('success')
            return redirect('products_page')

def delete_product(request,p):
      prdct=product.objects.get(id=p)
      prdct.delete()
      return redirect('products_page')

def edit_product_page(request,p):
      categories=category.objects.all()
      prdct=product.objects.get(id=p)
      return render(request,'admin/edit_product.html',{'product':prdct,'category':categories})