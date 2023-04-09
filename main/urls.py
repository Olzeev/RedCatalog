from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='shop'),
    path('catalog', views.catalog, name='catalog'),
    path('stock', views.stock, name='aktsii'),
    path('favourites', views.favourites, name='fav'),
    path('product/<int:pk>', views.product_page, name='product_page'),
    path('buy_product/<str:key>', views.buy_product, name='buy_product'),
    path('category/<str:key>', views.category_page, name='category_page'),
    path('login', views.login, name='login'),
    path('registration', views.registration, name='registration'),
    path('profile/general_data', views.profile_general_data, name='profile_general_data'),
    path('profile/sign_out', views.sign_out, name='sign_out'),
    path('profile/edit_data', views.profile_edit_data, name='profile_edit_data'),
    path('profile/purchase_history', views.profile_purchase_history, name='profile_purchase_history'),
    path('profile/sell_history', views.profile_sell_history, name='profile_sell_history'),
    path('profile/my_products', views.profile_my_products, name='profile_my_products'),
    path('profile', views.profile, name='profile'),
    path("add_to_favourites/<int:key>", views.add_to_favourites, name='add_to_favourites'),
]
