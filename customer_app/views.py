from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .models import customer_model
from products_app.models import product
from django.contrib.auth import login

# Create your views here.

def customer_home(request):
      products=product.objects.all()
      return render(request,'customer/home.html',{'products':products})

def registration_page(request):
      return render(request,'customer/register.html')

def login_page(request):
      return render(request,'customer/login.html')


def register(request):
      if request.method=='POST':
            first_name=request.POST['firstname']
            last_name=request.POST['lastname']
            user_name=request.POST['username']
            address=request.POST['address']
            phone=request.POST['phone']
            email=request.POST['email']
            photo=request.FILES.get('photo')
            # print(first_name,last_name,user_name,address,phone,email,photo)
            if User.objects.filter(username=user_name):
                  msg='Sorry the the username already exists....'
                  print('user exists')
                  return render(request,'customer/register.html',{'msg':msg,'fname':first_name,'lname':last_name,'email':email,'phone':phone,'user_name':user_name})
            else:
                  pass_word=request.POST['password']
                  c_pass_word=request.POST['c_password']

                  if pass_word==c_pass_word:
                        if User.objects.filter(username=user_name):
                              return redirect('customer_home')
                        else:
                              user=User.objects.create_user(
                                    first_name=first_name,
                                    last_name=last_name,
                                    email=email,
                                    username=user_name,
                                    password=pass_word,
                              )
                              user.save()
                              new_customer=customer_model(c_user=user,phone=phone,address=address,image=photo)
                              new_customer.save()
                              print('success')     
                              # success='Sign up successful...'
                              # title='Congratulations..'
                              # text='you have successfully registered.Your username and password is sent to to your email adress'
                              # icon='success'

                              # #sending mail
                              
                              # subject = 'Welcome to Eventia'
                              # message = 'Thank you for registering , your username is '+user_name+' and password is '+pass_word
                              # email_from = settings.EMAIL_HOST_USER
                              # recipient_list = [user.email, ]
                              # send_mail( subject, message, email_from, recipient_list)
                              return redirect('login_page')
                              # return render(request,'home.html',{'events':e,'success':success,'title':title,'text':text,'icon':icon})

                  else:
                        print('password not matchig....')
                        return redirect('customer_home')                              

      else:
                  print('hello')
                  return redirect('customer_home')


def user_login(request):
      if request.method=='POST':
            user_name=request.POST['user_name']
            pass_word=request.POST['pass_word']
            user=auth.authenticate(username=user_name,password=pass_word)
            if user is not None:
                  if user.is_staff:
                        login(request,user)
                        title="Success"
                        text='Signin successfull...'
                        icon='success'
                        return render(request,'admin/admin_home.html')
                        # return render(request,'admin_home.html',{'title':title,'text':text,'icon':icon})
                  else:
                        login(request,user)
                        auth.login(request,user)
                        s='s'
                        title="Success"
                        text='Signin successfull...'
                        icon='success'
                        return redirect('profile_page')
            else:
                  success='The username and password is not matching....'
                  title='Sorry'
                  text='The username and password is not matching...'
                  icon='warning'
                  print('failed')
                  return redirect('login_page')
                  # return render(request,'login.html',{'events':e,'success':success,'title':title,'text':text,'icon':icon})
      else:
            return redirect('customer_home')


def profile_page(request):
      if request.user.is_authenticated:
            current_user=request.user
            username=current_user.username
            print(current_user,username)
            profile=customer_model.objects.get(c_user=current_user)
            return render(request,'customer/profile.html',{'profile':profile})

def user_logout(request):
      auth.logout(request)
      return redirect('customer_home')

def cart_page(request):
      return render(request,'customer/cart.html')