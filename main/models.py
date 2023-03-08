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