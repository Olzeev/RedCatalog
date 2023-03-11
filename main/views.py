from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Products, Users
from django.views.generic.detail import DetailView
from .forms import UsersForm


def convert_prices(products):
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


def index(request):
    products = Products.objects.order_by("-percent_discount")
    convert_prices(products)
    return render(request, 'main/index.html', {"top_products": products[:5], "products": products[5:]})


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
    error = ''
    error_code = -1       # -1: нет ошибок, 0: нет такого пользователя, 1: неверный пароль
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        users = Users.objects.all()
        flag = False
        for i in users:
            if i.email == email and i.password == password:
                flag = True
                break
            elif i.email == email:
                flag = False
                error_code = 1
                error = 'Неверный пароль'
                break
        if flag:
            return redirect("shop")
        else:
            if error_code == -1:
                error = 'Пользователь с таким логином не найден'
                error_code = 0

    return render(request, 'main/login_page.html', {"error": error, "error_code": error_code})


def registration(request):
    error = ""
    error_code = -1     # -1: ошибок нет, 0: почта уже зарегистрирована
    if request.method == "POST":
        form = UsersForm(request.POST)
        users = Users.objects.all()
        flag = True
        for i in users:
            if i.email == form["email"].value():
                flag = False
                error = "Пользователь с такой электронной почтой уже зарегистрирован"
                error_code = 0
                break
        if form.is_valid() and flag:
            form.save()
            return redirect("shop")

    form = UsersForm()
    return render(request, 'main/registration_page.html', {"form": form, "error": error, "error_code": error_code})
