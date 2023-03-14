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
    count = models.IntegerField("Количество товара (в шк)", default=1)
    seller = models.CharField("Продавец", default="Red Catalog", max_length=40)

    def __str__(self):
        return f"{self.product_name} ({self.brand}, {self.price} руб)"

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Users(models.Model):
    email = models.CharField("Электронная почта", max_length=50)
    password = models.CharField("Пароль", max_length=35)
    user_name = models.CharField("Имя", max_length=25, default='', blank=True)
    user_surname = models.CharField("Фамилия", max_length=25, default='', blank=True)
    img_link = models.URLField("Ссылка на изображение для аватарки", default='', blank=True)
    age = models.IntegerField("Возраст", default=-1, blank=True)
    city = models.CharField("Город", max_length=40, default='', blank=True)
    money = models.IntegerField("Баланс", default=100000)
    products_purchased = models.IntegerField('Количество купленных товаров', default=0)
    products_sold = models.IntegerField('Колчество проданных товаров', default=0)
    money_earned = models.IntegerField('Заработок на продажах', default=0)
    money_spend = models.IntegerField('Потрачено на покупки', default=0)

    def __str__(self):
        if self.user_name:
            if self.user_surname:
                return f"{self.user_name} {self.user_surname}"
            else:
                return f"{self.user_name}"
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


class Purchased(models.Model):
    id_user = models.IntegerField("ID пользователя")
    id_product = models.IntegerField("ID товара")

    def __str__(self):
        return f"{self.id_user} -> {self.id_product}"

    class Meta:
        verbose_name = "Купленное"
        verbose_name_plural = "Купленное"


class Sold(models.Model):
    id_user = models.IntegerField("ID пользователя")
    id_product = models.IntegerField("ID товара")

    def __str__(self):
        return f"{self.id_user} -> {self.id_product}"

    class Meta:
        verbose_name = "Проданное"
        verbose_name_plural = "Проданное"


class Card(models.Model):
    id_user = models.IntegerField("ID пользователя")
    id_product = models.IntegerField("ID товара")

    def __str__(self):
        return f"{self.id_user} -> {self.id_product}"

    class Meta:
        verbose_name = "Карзины"
        verbose_name_plural = "Карзины"
