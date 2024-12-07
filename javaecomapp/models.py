
from django.db import models
import datetime

#Categories of products
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

#   End Categories


    #Castomer Data
class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# End Customer Data


    #Product Details
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=250, default='',blank=True, null=True)
    image = models.ImageField(upload_to='uploads/products/')

    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, max_digits=8, decimal_places=0)

    def __str__(self):
        return self.name


# End Product Details


    #order details
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=1)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=250, default='')
    phone = models.CharField(max_length=10)
    date_ordered = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.product.name} {self.quantity}'




#end order details








class Offers(models.Model):
    name = models.CharField(max_length=80)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/products/')



    def __str__(self):
        return self.name


class LatestBlog(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/products/')

    def __str__(self):
        return self.name



