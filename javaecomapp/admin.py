from django.contrib import admin
from .models import Category, Customer, Product, Order, Offers, LatestBlog

# Register your models here.
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Offers)
admin.site.register(LatestBlog)