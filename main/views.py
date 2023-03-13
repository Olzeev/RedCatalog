from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Products, Users
from django.views.generic.detail import DetailView
from .forms import UsersForm


def create_new_user(mail):
    user_new = User(None)
    user_new.is_registered = True
    user_new.mail = mail
    user_new.name = ''
    user_new.sname = ''
    user_new.age = -1
    user_new.city = ''
    user_new.money = 100000
    user_new.products_purchased = 0
    user_new.products_sold = 0
    user_new.money_earned = 0
    user_new.money_spend = 0
    user_new.img_link = ''
    return user_new


class User:
    def __init__(self, user):
        if user is None:
            self.is_registered = False
        else:
            self.mail = user.email
            self.is_registered = True
            self.name = user.user_name
            self.sname = user.user_surname
            self.age = user.age
            self.city = user.city
            self.money = user.money
            self.products_purchased = user.products_purchased
            self.products_sold = user.products_sold
            self.money_earned = user.money_earned
            self.money_spend = user.money_spend
            self.img_link = user.img_link

    def __str__(self):
        if self.is_registered:
            if self.name:
                if self.sname:
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


user = User(None)


def index(request):
    products = Products.objects.order_by("-percent_discount")
    convert_prices(products)
    return render(request, 'main/index.html', {"top_products": products[:5],
                                               "products": products[5:],
                                               "user_header": str(user),
                                               "user": user})


class Product_page(DetailView):
    model = Products
    template_name = 'main/product_page.html'
    context_object_name = 'product'

    def get_context_data(self, *args, **kwargs):
        context = super(Product_page,
                        self).get_context_data(*args, **kwargs)
        # add extra field
        context["user_header"] = str(user)
        context["user"] = user
        return context


def category_page(request, key):
    products = Products.objects.order_by("-percent_discount")

    return render(request, 'main/category_page.html', {"products": products,
                                                       "key": key,
                                                       "user_header": str(user),
                                                       "user": user})


def catalog(request):
    products = Products.objects.all()
    categories = sorted(set([i.category for i in products]))
    return render(request, 'main/catalog.html', {"products": categories,
                                                 "user_header": str(user),
                                                 "user": user})


def stock(request):
    products = Products.objects.order_by("-percent_discount")
    return render(request, 'main/stock.html', {"products": products,
                                               "user_header": str(user),
                                               "user": user})


def favourites(request):
    return render(request, 'main/favourites.html', {"user_header": str(user),
                                                      "user": user})


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
            user = User(user_found)

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
            global user
            form.save()
            user = create_new_user(form["email"].value())

            return redirect("shop")

    form = UsersForm()
    return render(request, 'main/registration_page.html', {"form": form, "error": error})


def profile(request):
    return render(request, 'main/profile/profile_general_data.html', {"user_header": str(user),
                                                                      "is_registered": user.is_registered,
                                                                      "user": user})


def sign_out(request):
    global user
    user = User(None)
    return redirect('shop')


def profile_general_data(request):
    return render(request, 'main/profile/profile_general_data.html', {"user_header": str(user),
                                                                      "is_registered": user.is_registered,
                                                                      "user": user})


def profile_edit_data(request):
    return render(request, 'main/profile/profile_edit_data.html', {"user_header": str(user),
                                                                      "is_registered": user.is_registered,
                                                                      "user": user})


def profile_purchase_history(request):
    return render(request, 'main/profile/profile_purchase_history.html', {"user_header": str(user),
                                                                      "is_registered": user.is_registered,
                                                                      "user": user})


def profile_sell_history(request):
    return render(request, 'main/profile/profile_sell_history.html', {"user_header": str(user),
                                                                      "is_registered": user.is_registered,
                                                                      "user": user})


def profile_my_products(request):
    return render(request, 'main/profile/profile_my_products.html', {"user_header": str(user),
                                                                      "is_registered": user.is_registered,
                                                                      "user": user})


class Buy_product(DetailView):
    model = Products
    template_name = 'main/buy_product.html'
    context_object_name = 'product'

    def get_context_data(self, *args, **kwargs):
        context = super(Buy_product,
                        self).get_context_data(*args, **kwargs)
        # add extra field
        context["user_header"] = str(user)
        context["user"] = user
        return context
