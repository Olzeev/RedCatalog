from .models import Users, Purchased, Products
from django.forms import ModelForm, TextInput


class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = ["email", "password"]

        widgets = {
            "email": TextInput(attrs={
                "class": "login_input",
                "placeholder": "Эл. почта",
                "type": "email",
                "maxlength": "30",
                "size": "30"
            }),
            "password": TextInput(attrs={
                "class": "password_input",
                "placeholder": "Пароль",
                "type": "password",
                "maxlength": "30",
                "size": "30"
            })
        }


class UsersRefactorForm(ModelForm):
    class Meta:
        model = Users
        fields = ["user_name", "user_surname", "age", "city", "img_file"]

        widgets = {
            "user_name": TextInput(attrs={
                "class": "login_input",
                "placeholder": "Имя",
                "maxlength": "30",
                "size": "30"
            }),
            "user_surname": TextInput(attrs={
                "class": "password_input",
                "placeholder": "Фамилия",
                "maxlength": "30",
                "size": "30"
            }),
            "age": TextInput(attrs={
                "class": "password_input",
                "placeholder": "Возраст",
                "maxlength": "30",
                "size": "30"
            }),
            "city": TextInput(attrs={
                "class": "password_input",
                "placeholder": "Город",
                "maxlength": "30",
                "size": "30"
            }),
            "img_file": TextInput(attrs={
                "class": "password_input",
                "placeholder": "Загрузить аватарку",
                "maxlength": "30",
                "size": "30"
            })
        }


class AddProductForm(ModelForm):
    class Meta:
        model = Products
        fields = ["product_name", "category", "brand", "description", "price", "count"]

        widgets = {
            "product_name": TextInput(attrs={
                "class": "text_input",
                "placeholder": "Название товара",
                "maxlength": "30",
                "size": "30"
            }),
            "category": TextInput(attrs={
                "class": "text_input",
                "placeholder": "Фамилия",
                "maxlength": "30",
                "size": "30"
            }),
            "brand": TextInput(attrs={
                "class": "text_input",
                "placeholder": "Возраст",
                "maxlength": "30",
                "size": "30"
            }),
            "description": TextInput(attrs={
                "class": "text_input",
                "placeholder": "Город",
                "maxlength": "30",
                "size": "30"
            }),
            "price": TextInput(attrs={
                "class": "text_input",
                "placeholder": "Загрузить аватарку",
                "maxlength": "30",
                "size": "30"
            }),
            "count": TextInput(attrs={
                "class": "text_input",
                "placeholder": "Загрузить аватарку",
                "maxlength": "30",
                "size": "30"
            })
        }