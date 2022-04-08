import email
from multiprocessing import context
from django.shortcuts import  render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import LoginForm
from products.models import *
from .filters import ProductFilter



def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'account created')
            return redirect('/register')
        else:
            messages.add_message(request,messages.ERROR,'please provide correct details')
            return render(request,'user/register.html',{
                'form':form

            })
    context={
        'form':UserCreationForm
    }
    return render(request,'users/register.html',context)


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user=authenticate(request,username=data['username'],
            password=data['password'])

            if user is not None:
                login(request,user)
                if user.is_staff:

                    return redirect('/admins/dashboard')
                else: 
                    return redirect('/')
            else:
                messages.add_message(request,messages.ERROR,'please provide correct credentials')
                return render(request,'users/login.html',{
                    'form':form
                }) 
    form = LoginForm    
    context={
        'form':form
    }  
    return render(request,'users/login.html',context)


def logout_user(request):
    logout(request)
    return redirect('/login')

   

def homepage(request):
    products= Product.objects.all().order_by('-id')[:6]
    category=Category.objects.all()
    e_book=BookNow.objects.all().order_by('-id')
    context ={
        'products':products,
        'e_book' :e_book,
        'category':category
        
    }
    return render(request,'users/index.html',context)


def productspage(request):
    products= Product.objects.all().order_by('-id')
    product_filter=ProductFilter(request.GET,queryset=products)
    product_final=product_filter.qs
    context ={
        'products':product_final,
        'product_filter':product_filter
    }
    return render(request,'users/products.html',context)

def product_detail(request,product_id):
    products=Product.objects.get(id=product_id)
    context={
        'products':products
    }
    return render(request,'users/productdetails.html',context)
    

def ebook_detail(request,id):
    e_book=BookNow.objects.get(id=id)
    context={
        'e_book':e_book
    }
    return render(request,'users/pdfdetails.html',context)









