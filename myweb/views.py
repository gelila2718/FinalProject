from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views.generic import View
from .models import Product


# def home(request):
#     Products = Product.objects.all()[:1]
#     context = {"featured_products": Products}
#     return render(request, "home.html", context)


def home(request):
    products = Product.objects.all()  # Assuming you want to display all products
    return render(request, "home.html", {"products": products})


def AboutPageView(request):
    return render(request, "about.html")


def ContactPageView(request):
    return render(request, "contact.html")


def view_item(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    all_products = Product.objects.all()
    return render(request, "view_item.html", {"product": product})


def StorePageView(request):
    products = Product.objects.all()
    return render(request, "store.html", {"products": products})
