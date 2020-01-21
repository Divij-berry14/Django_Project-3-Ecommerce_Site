from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'shop/index.html')

def about(request):
    return HttpResponse("About Us")

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

