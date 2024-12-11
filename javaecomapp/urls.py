from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about',views.about,name='about'),
    path('contact-us',views.contact,name='contact'),
    path('checkout',views.checkout,name='checkout'),

    path('gallery',views.gallery,name='gallery'),
    path('my-account',views.my_account,name='my_account'),
    path('shop',views.shop,name='shop'),
    path('shop2',views.shop2,name='shop2'),
    path('wishlist',views.wishlist,name='wishlist'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register',views.register_user,name='register'),
    path('product/<int:pk>', views.product, name='product'),
    path('search', views.search, name='search'),
    path('update_user', views.update_user, name='update_user'),

]