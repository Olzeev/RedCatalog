from django.contrib import admin
from .models import Products, Users, Favourites, Sold, Cart, Purchased

admin.site.register(Products)
admin.site.register(Users)
admin.site.register(Favourites)
admin.site.register(Purchased)
admin.site.register(Cart)
admin.site.register(Sold)

