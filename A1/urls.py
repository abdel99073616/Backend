from django.urls import path
from .views import *
urlpatterns = [
        path('', home, name='home'),
        path('login/', loginpage, name='login'),
        path('register/', registerpage, name='register'),
        path('logout/', logoutpage, name='logout'),

        path('product/', Prodects, name='product'),
        path('user/' , userpage , name='user-page'),
        path('customer/<str:pk>', Customers, name='customer'),
        path('create_order/<str:pk>', createOrder, name='create_order'),
        path('update_order/<str:pk>', updateOrder, name='update_order'),
        path('delete/<str:pk>', deleteOrder, name='delete_order'),
        path('account/', deleteOrder, name='account')
]
