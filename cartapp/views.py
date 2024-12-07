

from django.http import JsonResponse
from javaecomapp.models import Product
# # from DjangomainApp.views import product
from .cart import Cart
from django.shortcuts import render, get_object_or_404

# Create your views here.
def cart_summary(request):
    #get the cart
    cart = Cart(request)
    cart_products = cart.get_prods()
    return render(request,'cart_summary.html', {'cart_products':cart_products})



def cart_add(request):
    # #get the cart
    cart = Cart(request)
    #test for POST
    if request.POST.get('action') == 'post':
        #Get staff
        product_id = int(request.POST.get('product_id'))
        # product_qty = int(request.POST.get('product_qty'))
        #look product in the DB
        product = get_object_or_404(Product, id=product_id)
        #sev to session
        cart.add(product=product)

        # Get cart quantity
        cart_quantity = cart.__len__()

        #Return response
        # response = JsonResponse({'Product Name:' : product.name})
        response = JsonResponse({'qty:': cart_quantity})
        return response

def cart_delete(request):
    pass

def cart_update(request):
    pass
