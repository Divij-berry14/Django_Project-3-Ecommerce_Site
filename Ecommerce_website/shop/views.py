from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil
def index(request):
    products=Product.objects.all()
    print(products)
    n=len(products)
    nSlides=n//4 +ceil((n/4) -(n//4))
    param={'No. of Slides':nSlides,'range':range(nSlides),'product':products}
    return render(request,'shop/index.html',param)

def about(request):
    return render(request,'shop/about.html')
def contact(request):
    return HttpResponse("If any queries, kindly contact us!")

def tracker(request):
    return HttpResponse("Track your Order")

def search(request):
    return HttpResponse("Please Search an item")

def checkout(request):
    return HttpResponse("Proceed to Checkout")

def prodView(request):
    return HttpResponse("Please view your Product")

