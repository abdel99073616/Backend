from django.urls import path
from .views import home, Customers, Prodects, createOrder, updateOrder, deleteOrder
urlpatterns = [
        path('', home, name='home'),
        path('customer/<str:pk>', Customers, name='customer'),
        path('product/', Prodects, name='product'),
        path('create_order/<str:pk>', createOrder, name='create_order'),
        path('update_order/<str:pk>', updateOrder, name='update_order'),
        path('delete/<str:pk>', deleteOrder, name='delete_order'),
        path('logout/', home, name='logout'),
]

