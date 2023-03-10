from django.http import HttpResponse
from django.shortcuts import render
from .models import Products
from django.views.generic.detail import DetailView


def index(request):
    products = Products.objects.filter().order_by("-percent_discount")[:5]
    for i in products:
        cnt = 1
        new_price = ''
        for c in str(i.price)[::-1]:
            new_price += c
            if cnt % 3 == 0:
                new_price += ' '
            cnt += 1
        i.price = new_price[::-1]
        cnt = 1
        new_price = ''

        for c in str(i.price_with_discount)[::-1]:
            new_price += c
            if cnt % 3 == 0:
                new_price += ' '
            cnt += 1

        i.price_with_discount = new_price[::-1]
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


def login(request):
    return render(request, 'main/login_page.html')


def registration(request):
    return render(request, 'main/registration_page.html')
