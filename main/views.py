from django.http import HttpResponse
from django.shortcuts import render
from .models import Products
from django.views.generic.detail import DetailView

# new comment
# new comment 2
# new comment 3
# new comment 4
# new comment 5
# new comment 6

# new comment 7

def index(request):
    products = Products.objects.order_by("-percent_discount")

    return render(request, 'main/index.html', {"products": products})


class Product_page(DetailView):
    model = Products
    template_name = 'main/product_page.html'
    context_object_name = 'product'


def category_page(request, key):
    products = Products.objects.order_by("-percent_discount")

    return render(request, 'main/category_page.html', {"products": products, "key": key})


def catalog(request):
    products = Products.objects.all()
    categories = sorted(set([i.category for i in products]))
    return render(request, 'main/catalog.html', {"products": categories})


def stock(request):
    products = Products.objects.order_by("-percent_discount")
    return render(request, 'main/stock.html', {"products": products})


def favourites(request):
    return render(request, 'main/favourites.html')
