from concurrent.futures import process
import email
from email import message
from multiprocessing import context
from sqlite3 import adapt
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from users.models import Contact
from .forms import LoginForm
from products.models import *
from .filters import ProductFilter
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage, send_mail
from ecommerce import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from . tokens import generate_token


def register_user(request):
    if request.method == "POST":
        username = request.POST['username']
        name = request.POST['name']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(
                request, "Username already exist! Please try some other username.")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('register')

        if len(username) > 20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('register')

        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('register')

        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('register')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.name = name
        # myuser.is_active = False
        myuser.is_active = False
        myuser.save()
        messages.success(
            request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")

        # Welcome Email
        subject = "Welcome to GFG- Django Login!!"
        message = "Hello " + myuser.name + "!! \n" + "Welcome to GFG!! \nThank you for visiting our website\n. We have also sent you a confirmation email, please confirm your email address. \n \nThanking You\nAnubhav Madhav"
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

        # Email Address Confirmation Email
        current_site = get_current_site(request)
        email_subject = "Confirm your Email @ GFG - Django Login!!"
        message2 = render_to_string('email_confirmation.html', {

            'name': myuser.name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })
        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email],
        )
        email.fail_silently = True
        email.send()

        return redirect('login')

    return render(request, "users/register.html")


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()
        login(request, myuser)
        messages.success(request, "Your Account has been activated!!")
        return redirect('login')
    else:
        return render(request, 'activation_failed.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            name = user.first_name
            # messages.success(request, "Logged In Sucessfully!!")
            return redirect( "/admins/dashboard/",{"name":name})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('login')
    
    return render(request, "users/login.html")


def logout_user(request):
    logout(request)
    return redirect('/login')


def homepage(request):
    products = Product.objects.all().order_by('-id')[:8]
    category = Category.objects.all()
    e_book = BookNow.objects.all().order_by('-id')[:4]
    categories = Category.objects.all()
    
    context = {
        'products': products,
        'e_book': e_book,
        'category': category,
        'categories':categories

    }
    return render(request, 'users/index.html', context)


def productspage(request):
    products = Product.objects.all().order_by('-id')
    product_filter = ProductFilter(request.GET, queryset=products)
    product_final = product_filter.qs
    context = {
        'products': product_final,
        'product_filter': product_filter
    }
    return render(request, 'users/products.html', context)

def indexsearch(request):
    products = Product.objects.all().order_by('-id')
    product_filter = ProductFilter(request.GET, queryset=products)
    product_final = product_filter.qs
    context = {
        'products': product_final,
        'product_filter': product_filter
    }
    return render(request, 'users/index.html', context)


def product_detail(request, product_id):
    products = Product.objects.get(id=product_id)
    context = {
        'products': products
    }
    return render(request, 'users/productdetails.html', context)


def ebook_detail(request, id):
    e_book = BookNow.objects.get(id=id)
    context = {
        'e_book': e_book
    }
    return render(request, 'users/pdfdetails.html', context)



def category_to_post(request,category_id):
    products1 = Product.objects.all()
    products = Product.objects.get(id=category_id)
    context={
        'products1':products1,
        'products':products,
        'category':category,
    }
    return render(request, 'users/category_id_post.html',context)

def contactus(request):
    if request.method=="GET":
        return render(request, 'users/contactus.html')
    elif request.method=="POST":
        name=request.POST["name"] 
        email=request.POST["email"]
        subject=request.POST["subject"]
        message=request.POST["desc"]
        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        return redirect("/")

def aboutus(request):
    if request.method=="GET":
        return render(request, 'users/aboutus.html')