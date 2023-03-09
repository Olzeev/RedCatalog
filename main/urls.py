from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='shop'),
    path('catalog', views.catalog, name='catalog'),
    path('stock', views.stock, name='aktsii'),
    path('favourites', views.favourites, name='fav'),
    path('product/<int:pk>', views.Product_page.as_view(), name='product_page'),
    path('category/<str:key>', views.category_page, name='category_page'),
    path('login', views.login, name='login'), #вход
    path('registration', views.registration, name='registration')
]
