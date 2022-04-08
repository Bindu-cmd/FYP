from itertools import product
from django.contrib import admin
from . models import *

# Register your models here.
#paila file ko name ani class ko name 
#class ko name jaile capital ma hunxa

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(BookNow)
admin.site.register(Language)
