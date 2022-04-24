
from distutils.command.upload import upload
from itertools import product
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import *
from django.core import validators

# Create your models here.

class Category(models.Model):
    category_name =models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.FloatField()
    stock = models.IntegerField()
    image = models.FileField(upload_to='static/uploads',null=True)
    description=models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    authorname=models.CharField(max_length=100,null=True)
    

    def __str__(self):
        return self.product_name

    @staticmethod
    def get_all_products_by_id():
        return Product.objects.all()


class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    PAYMENT =(
        ('Cash On Delivery','Cash On Delivery'),
        ('Esewa','Esewa')
        
    )
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    total_price=models.IntegerField(null=True)
    status=models.CharField(default='Pending',max_length=200)
    payment_method=models.CharField(max_length=200,choices=PAYMENT)
    payment_status=models.BooleanField(default=False,null=True,blank=True)
    contact_no=models.CharField(validators=[MinLengthValidator(9),MaxLengthValidator(10)],max_length=10)
    address=models.CharField(max_length=200)
    created_date=models.DateTimeField(auto_now_add=True)


    

class BookNow(models.Model):
    bookname =models.CharField(max_length=255)
    authorname=models.CharField(max_length=100)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    publisher=models.CharField(max_length=200, blank=True)
    pages=models.IntegerField()
   
    description=models.TextField()
    publish_year=models.IntegerField()
    cover_image=models.ImageField(upload_to='static/pdfimage',null=True)
    pdf_file=models.FileField(upload_to='static/pdffile')


    def __str__(self):
        return self.bookname 
    
class Myrating(models.Model):
    user    = models.ForeignKey(User,on_delete=models.CASCADE)
    places  = models.ForeignKey(Product,on_delete=models.CASCADE)
    rating  = models.IntegerField(default=1,validators=[MaxValueValidator(5),MinValueValidator(0)])
    
    def __str__(self):
        return str(self.user)
   




    