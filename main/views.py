from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Products, Users
from django.views.generic.detail import DetailView
from .forms import UsersForm


class User:
    def __init__(self, is_registered, mail, name, sname):
        self.mail = mail
        self.is_registered = is_registered
        self.name = name
        self.sname = sname


    def __str__(self):
        if self.is_registered:
            if self.name is not None:
                if self.sname is not None:
                    return f"{self.name} {self.sname}"
                else:
                    return f"{self.name}"
            else:
                return self.mail
        else:
            return ''


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


user = User(False, None, None, None)


def index(request):
    products = Products.objects.order_by("-percent_discount")
    convert_prices(products)
    return render(request, 'main/index.html', {"top_products": products[:5],
                                               "products": products[5:],
                                               "user_header": str(user),
                                               "is_registered": user.is_registered})


class Product_page(DetailView):
    model = Products
    template_name = 'main/product_page.html'
    context_object_name = 'product'

    def get_context_data(self, *args, **kwargs):
        context = super(Product_page,
                        self).get_context_data(*args, **kwargs)
        # add extra field
        context["user_header"] = str(user)
        context["is_registered"] = user.is_registered
        return context


def category_page(request, key):
    products = Products.objects.order_by("-percent_discount")

    return render(request, 'main/category_page.html', {"products": products,
                                                       "key": key,
                                                       "user_header": str(user),
                                                       "is_registered": user.is_registered})


def catalog(request):
    products = Products.objects.all()
    categories = sorted(set([i.category for i in products]))
    return render(request, 'main/catalog.html', {"products": categories,
                                                 "user_header": str(user),
                                                 "is_registered": user.is_registered})


def stock(request):
    products = Products.objects.order_by("-percent_discount")
    return render(request, 'main/stock.html', {"products": products,
                                               "user_header": str(user),
                                               "is_registered": user.is_registered})


def favourites(request):
    return render(request, 'main/favourites.html', {"user_header": str(user),
                                                      "is_registered": user.is_registered})


def login(request):
    global user
    error = ''
    error_code = -1       # -1: нет ошибок, 0: нет такого пользователя, 1: неверный пароль
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        users = Users.objects.all()
        flag = False
        user_found = None
        for i in users:
            if i.email == email and i.password == password:
                flag = True
                user_found = i
                break
            elif i.email == email:
                flag = False
                error_code = 1
                error = 'Неверный пароль'
                break
        if flag:
            user.mail = user_found.email
            user.is_registered = True
            user.name = user_found.user_name if len(user_found.user_name) else None
            user.sname = user_found.user_surname if len(user_found.user_surname) else None

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
            form.save()
            user.mail = form["email"].value()
            user.is_registered = True
            return redirect("shop")

    form = UsersForm()
    return render(request, 'main/registration_page.html', {"form": form, "error": error})


def profile(request):
    return render(request, 'main/profile/profile_general_data.html', {"user_header": str(user),
                                                                      "is_registered": user.is_registered})


def sign_out(request):
    user.is_registered = False
    user.name, user.sname, user.mail = None, None, None
    return redirect('shop')


def profile_general_data(request):
    return render(request, 'main/profile/profile_general_data.html', {"user_header": str(user),
                                                                      "is_registered": user.is_registered})


def profile_edit_data(request):
    return render(request, 'main/profile/profile_edit_data.html', {"user_header": str(user),
                                                                      "is_registered": user.is_registered})


def profile_purchase_history(request):
    return render(request, 'main/profile/profile_purchase_history.html', {"user_header": str(user),
                                                                      "is_registered": user.is_registered})


def profile_sell_history(request):
    return render(request, 'main/profile/profile_sell_history.html', {"user_header": str(user),
                                                                      "is_registered": user.is_registered})


def profile_my_products(request):
    return render(request, 'main/profile/profile_my_products.html', {"user_header": str(user),
                                                                      "is_registered": user.is_registered})
