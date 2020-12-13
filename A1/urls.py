from django.contrib import admin
from django.urls import path , include
from .views import home ,Customers , Prodects,createOrder
urlpatterns = [
        path('', home , name = 'home'),
        path('customer/<str:pk>', Customers, name='customer'),
        path('product/', Prodects, name='product'),
        path('create_order/', createOrder, name='create_order'),
        path('logout/', home, name='logout'),
]
