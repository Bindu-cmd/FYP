from django.urls import URLPattern, path
from . import views

urlpatterns=[
    path('dashboard/',views.admin_home),
]