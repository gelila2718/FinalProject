from django.shortcuts import render, HttpResponse
from django.views.generic import View
from .models import Product


# Create your views here.
def home(request):
    return render(request, "home.html")


def AboutPageView(request):
    return render(request, "about.html")

def StorePageView(request):
    products = Product.objects.all()
    return render(request, "store.html", {"products": products})
