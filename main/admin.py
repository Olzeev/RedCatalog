from django.contrib import admin
from .models import Products, Users, Favourites, Sold, Card, Purchased

admin.site.register(Products)
admin.site.register(Users)
admin.site.register(Favourites)
admin.site.register(Purchased)
admin.site.register(Card)
admin.site.register(Sold)

