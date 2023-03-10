from django.contrib import admin
from .models import Products, Users, Favourites

admin.site.register(Products)
admin.site.register(Users)
admin.site.register(Favourites)
