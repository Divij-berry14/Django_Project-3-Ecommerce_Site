from django.contrib import admin
from django.urls import path
from . import views

app_name='shop'

urlpatterns=[
    path("",views.index,name='ShopHome'),
    path("about/",views.about,name='About'),
    path("contact/",views.contact,name='Contact Us'),
    path("tracker/",views.tracker,name='Tracking Status'),
    path("search/",views.search,name='Search'),
    path("productView/",views.prodView,name='Product View'),
    path("checkout/",views.checkout,name='Checkout'),
]