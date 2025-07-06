from django.shortcuts import render,HttpResponse,redirect
from .models import Sell,Order
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
import random

def index(request):
    return render(request,'index.html')

def generate_unique_product_id():
    while True:
        pid = random.randint(100000, 999999)
        if not Sell.objects.filter(product_id=pid).exists():
            return pid

def sell(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        item = request.POST.get('item')
        price = request.POST.get('price')
        description = request.POST.get('description') or "No description"
        image = request.FILES.get('image')

        Sell.objects.create(
            name=name,
            phone=phone,
            item=item,
            image=image,
            product_id=generate_unique_product_id(),
            price=price,
            description=description
            )
        messages.success(request, "Product uploaded successfully!")
        return redirect('/') 

    return render(request, 'sell.html')
def calci(request):
    products = Sell.objects.filter(item='calculator')
    return render(request, 'buy.html', {'products': products})
def apron(request):
    products = Sell.objects.filter(item='apron')
    return render(request, 'buy.html', {'products': products})
def etb(request):
    products = Sell.objects.filter(item='etb')
    return render(request, 'buy.html', {'products': products})
def projects(request):
    products = Sell.objects.filter(item='project')
    return render(request, 'buy.html', {'products': products})
def others(request):
    products = Sell.objects.filter(item='others')
    return render(request, 'buy.html', {'products': products})
def order_view(request,product_id):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        product_id = request.POST.get('product_id')
        Order.objects.create(
            name=name,
            phone=phone,
            product_id=product_id,
        )
        messages.success(request, "Order placed successfully!")
        return redirect('/') 
    return render(request,'order.html',{'product_id' : product_id})