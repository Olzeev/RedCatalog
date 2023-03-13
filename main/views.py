from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Products, Users
from django.views.generic.detail import DetailView
from .forms import UsersForm, UsersRefactorForm


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


class Product_page(DetailView):
    model = Products
    template_name = 'main/product_page.html'
    context_object_name = 'product'

    def get_context_data(self, *args, **kwargs):
        context = super(Product_page,
                        self).get_context_data(*args, **kwargs)
        user = sign_in_user(email_user_in_account)
        # add extra field
        context["user_header"] = str(user)
        context["user"] = user
        context["user_in_account"] = user_in_account
        return context


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
    return render(request, 'main/profile/profile_purchase_history.html', {"user_header": str(user),
                                                                      "user": user,
                                                                      "user_in_account": user_in_account})


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


class Buy_product(DetailView):
    model = Products
    template_name = 'main/buy_product.html'
    context_object_name = 'product'

    def get_context_data(self, *args, **kwargs):
        context = super(Buy_product,
                        self).get_context_data(*args, **kwargs)
        user = sign_in_user(email_user_in_account)
        # add extra field
        context["user_header"] = str(user)
        context["user"] = user
        context["user_in_account"] = user_in_account
        return context
