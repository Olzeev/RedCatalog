from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Products, Users, Purchased, Favourites
from django.views.generic.detail import DetailView
from .forms import UsersForm, UsersRefactorForm
from django.conf import settings
from django.core.mail import send_mail
import random

def sign_in_user(email=''):
    users = Users.objects.all()
    for i in users:
        if i.email == email:
            return i
    return ""


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


user_in_account = False
email_user_in_account = ''


def index(request):
    products = Products.objects.order_by("-percent_discount")
    convert_prices(products)
    user = sign_in_user(email_user_in_account)
    return render(request, 'main/index.html', {"top_products": products[:5],
                                               "products": products[5:],
                                               "user_header": str(user),
                                               "user": user,
                                               "user_in_account": user_in_account})


def product_page(request, pk):
    product = Products.objects.get(id=pk)
    user = sign_in_user(email_user_in_account)
    in_favourite = False
    if user and Favourites.objects.filter(id_user=user.id, id_product=pk):
        in_favourite = True
    data = {'product': product, "user_header": str(user), "user": user, "user_in_account": user_in_account, 'in_favourite': in_favourite}
    return render(request, 'main/product_page.html', data)


def buy_product(request, key):
    product = Products.objects.get(id=key)
    user = sign_in_user(email_user_in_account)
    price = product.price
    if product.discount:
        price = product.price_with_discount
    if user.money >= price:
        user_buy_product = Purchased()
        user_buy_product.id_user = user.id
        user_buy_product.id_product = key
        user_buy_product.save()

        user.money -= price
        user.save()

        product.count -= 1
        product.save()

        data = {'product': product, "user_header": str(user), "user": user, "user_in_account": user_in_account}
        return render(request, 'main/product_success.html', data)
    return render(request, 'main/index.html')


def category_page(request, key):
    products = Products.objects.order_by("-percent_discount")
    user = sign_in_user(email_user_in_account)
    return render(request, 'main/category_page.html', {"products": products,
                                                       "key": key,
                                                       "user_header": str(user),
                                                       "user": user,
                                                       "user_in_account": user_in_account})


def catalog(request):
    products = Products.objects.all()
    categories = sorted(set([i.category for i in products]))
    user = sign_in_user(email_user_in_account)
    return render(request, 'main/catalog.html', {"products": categories,
                                                 "user_header": str(user),
                                                 "user": user,
                                                 "user_in_account": user_in_account})


def stock(request):
    products = Products.objects.order_by("-percent_discount")
    user = sign_in_user(email_user_in_account)
    return render(request, 'main/stock.html', {"products": products,
                                               "user_header": str(user),
                                               "user": user,
                                               "user_in_account": user_in_account})


def favourites(request):
    user = sign_in_user(email_user_in_account)
    return render(request, 'main/favourites.html', {"user_header": str(user),
                                                    "user": user,
                                                    "user_in_account": user_in_account})


def login(request):
    global user_in_account
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
            global user_in_account, email_user_in_account
            user_in_account = True
            email_user_in_account = email
            return redirect("shop")
        else:
            if error_code == -1:
                error = 'Пользователь с таким логином не найден'
                error_code = 0

    return render(request, 'main/login_page.html', {"error": error, "error_code": error_code})


def registration(request):

    error = ""
    if request.method == "POST":
        form = UsersForm(request.POST)
        users = Users.objects.all()
        flag = True
        for i in users:
            if i.email == form["email"].value():
                flag = False
                error = "Пользователь с такой электронной почтой уже зарегистрирован"
                break
        if form.is_valid() and flag:
            global user_in_account, email_user_in_account
            form.save()
            user_in_account = True
            email_user_in_account = form["email"].value()
            return redirect("shop")

    form = UsersForm()
    return render(request, 'main/registration_page.html', {"form": form, "error": error})


def profile(request):
    user = sign_in_user(email_user_in_account)
    purchased = Purchased.objects.filter(id_user=user.id)
    purchased_money = 0
    purchased_count = 0
    for i in purchased:
        purchased_count += 1
        product = Products.objects.get(id=i.id_product)
        price = product.price
        if product.discount:
            price = product.price_with_discount
        purchased_money += price
        user.products_purchased = purchased_count
        user.money_spend = purchased_money
    return render(request, 'main/profile/profile_general_data.html', {"user_header": str(user),
                                                                      "user": user,
                                                                      "user_in_account": user_in_account})


def sign_out(request):
    global user_in_account
    user_in_account = False
    return redirect('shop')


def profile_general_data(request):
    user = sign_in_user(email_user_in_account)

    return render(request, 'main/profile/profile_general_data.html', {"user_header": str(user),
                                                                      "user": user,
                                                                      "user_in_account": user_in_account})


def profile_edit_data(request):
    user = sign_in_user(email_user_in_account)
    user_refactor = Users.objects.get(id=user.id)
    if request.method == "POST":
        form = UsersRefactorForm(request.POST)
        if form.is_valid():
            if form['user_name'].value() != '':
                user_refactor.user_name = form['user_name'].value()
            if form['user_surname'].value() != '':
                user_refactor.user_surname = form['user_surname'].value()
            if form['age'].value() != '':
                user_refactor.age = int(form['age'].value())
            if form['city'].value() != '':
                user_refactor.city = form['city'].value()
            user_refactor.save()
            return redirect("shop")

    form = UsersRefactorForm()
    return render(request, 'main/profile/profile_edit_data.html', {"user_header": str(user),
                                                                    "user": user,
                                                                    "user_in_account": user_in_account,
                                                                    "form": form})


def profile_purchase_history(request):
    user = sign_in_user(email_user_in_account)
    purchased_user = Purchased.objects.filter(id_user=user.id)
    id_date_products_purchased = []
    for i in purchased_user:
        id_date_products_purchased.append([i.id_product, i.date])
    print(id_date_products_purchased)
    products_purchased = []
    for id_product, date in id_date_products_purchased:
        product = Products.objects.get(id=id_product)
        products_purchased.append([product, date])
    return render(request, 'main/profile/profile_purchase_history.html', {"user_header": str(user),
                                                                      "user": user,
                                                                      "user_in_account": user_in_account,
                                                                      "products_purchased": products_purchased[::-1]})


def profile_sell_history(request):
    user = sign_in_user(email_user_in_account)
    return render(request, 'main/profile/profile_sell_history.html', {"user_header": str(user),
                                                                      "user": user,
                                                                      "user_in_account": user_in_account})


def profile_my_products(request):
    user = sign_in_user(email_user_in_account)
    return render(request, 'main/profile/profile_my_products.html', {"user_header": str(user),
                                                                      "user": user,
                                                                      "user_in_account": user_in_account})


def add_to_favourites(request, key):
    user = sign_in_user(email_user_in_account)
    connection = Favourites.objects.filter(id_user=user.id, id_product=key)
    if connection:
        connection[0].delete()
        return redirect("product_page", key)
    product_add_to_favourite = Favourites()
    product_add_to_favourite.id_product = key
    product_add_to_favourite.id_user = user.id
    product_add_to_favourite.save()
    return redirect("product_page", key)