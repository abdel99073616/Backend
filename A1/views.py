from django.shortcuts import render , redirect
from django.urls import path , include
from .models import (
    Product,
    Customer,
    Order,
)
from .forms import OrderForm
def home(request):
    order = Order.objects.all()
    customers = Customer.objects.all()
    total_customer = Customer.objects.count()
    total_order = Order.objects.count()
    delivered = order.filter('Delivered').count()
    pending = order.filter('Pending').count()

    context = {'customers' : customers,
               'order':order,
               'total_customer' : total_customer,
               'delivered':delivered,
               'pending':pending
               }
    return render(request,'accounts/dashboard.html')


def Customers(request,pk):
    customer = Customer.objects.get(id=pk)
    orders =customer.order_set.all()
    orders_count = orders.count()
    context = {'customer':customer , 'orders':orders, 'orders_count':orders_count}
    return render(request,'accounts/customer.html',{'context':context})

def Prodects(request):
    products = Product.objects.all()
    return render(request,'accounts/products.html',{'products' : products})
def createOrder(request):
    form = OrderForm(request.POST)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context ={'form' : form}
    return render(request,'accounts/order_form.html',{'context':context})
