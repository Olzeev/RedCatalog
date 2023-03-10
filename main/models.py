from django.db import models


class Products(models.Model):
    product_name = models.CharField("Название товара", max_length=100)
    description = models.TextField("Описание товара")
    brand = models.CharField("Название бренда производителя", max_length=50)
    category = models.CharField("Категория", max_length=40)
    img_link = models.TextField("Ссылка на изображение", default='')
    price = models.IntegerField("Цена")
    discount = models.BooleanField("Есть ли скидка на товар", default=False)
    price_with_discount = models.IntegerField("Цена со скидкой")
    percent_discount = models.IntegerField("Процент скидки", default=0)

    def __str__(self):
        return f"{self.product_name} ({self.brand}, {self.price} руб)"

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Users(models.Model):
    email = models.CharField("Электронная почта", max_length=50)
    login = models.CharField("Логин", max_length=35)
    user_name = models.CharField("Имя", max_length=25, default='')
    user_surname = models.CharField("Фамилия", max_length=25, default='')
    age = models.IntegerField("Возраст", default=18)
    sity = models.CharField("Город", max_length=40, default='')
    money = models.IntegerField("Баланс", default=100000)
    flag = models.BooleanField("Продавец или нет", default=False)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Favourites(models.Model):
    id_user = models.IntegerField("ID пользователя")
    id_product = models.IntegerField("ID товара")

    def __str__(self):
        return f"{self.id_user} -> {self.id_product}"

    class Meta:
        verbose_name = "Избранное"
        verbose_name_plural = "Избранное"

