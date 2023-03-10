from .models import Users
from django.forms import ModelForm, TextInput


class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = ["email", "login"]

        widgets = {
            "email": TextInput(attrs={
                "class": "login_input",
                "placeholder": "Эл. почта",
                "type": "email",
                "maxlength": "30",
                "size": "30"
            }),
            "login": TextInput(attrs={
                "class": "password_input",
                "placeholder": "Пароль",
                "type": "password",
                "maxlength": "30",
                "size": "30"
            })
        }