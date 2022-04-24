from unicodedata import name
from django.urls import URLPattern, path 
from .import views



urlpatterns=[
    path('register/',views.register_user,name='register'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('',views.homepage,name=''),
    path('allproducts/', views.productspage,name='allproducts'),
    path('productdetails/<int:product_id>', views.product_detail,name='productdetails'),
    path('pdfdetails/<int:id>', views.ebook_detail,name='pdfdetails'),
    path('category_to_post/<int:category_id>', views.category_to_post,name='category_to_post'),
  

    path('contactus', views.contactus, name='contactus'),
    path('aboutus', views.aboutus, name='aboutus'),

]