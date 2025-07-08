from django.shortcuts import render,HttpResponse,redirect
from .models import Sell,Order
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
import random
from django.core.mail import send_mail
from django.conf import settings

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
        email = request.POST.get('email') 
        item = request.POST.get('item')
        price = request.POST.get('price')
        description = request.POST.get('description') or "No description"
        image = request.FILES.get('image')

        Sell.objects.create(
            name=name,
            phone=phone,
            email=email,
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
        product = Sell.objects.get(product_id=product_id)
        Order.objects.create(
            name=name,
            phone=phone,
            product_id=product_id,
        )
        subject = "Your product has been ordered!"
        message = f"""
Hello {product.name},

Your product {product.item} with ID {product.product_id} has been ordered.

Order Details:
 Buyer Name: {name}
 Buyer Phone Number: {phone}
 Product: {product.item}
 Price: ₹{product.price}

Please coordinate further with the buyer.

Thank you,
82_WORN Team
"""
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [product.email],
            fail_silently=False,
        )

        product.delete()
        messages.success(request, "Order placed successfully!")
        return redirect('/') 
    return render(request,'order.html',{'product_id' : product_id})