
from django.contrib import messages
from django.http import JsonResponse
from javaecomapp.models import Product
# # from DjangomainApp.views import product
from .cart import Cart
from django.shortcuts import render, get_object_or_404, redirect








# Create your views here.
def cart_summary(request):
    #get the cart
    cart = Cart(request)
    cart_products = cart.get_prods()
    quantities = cart.get_quants()
    totals = cart.cart_total()
    return render(request,'cart_summary.html', {'cart_products':cart_products, 'quantities':quantities, 'totals':totals})



def cart_add(request):
    # #get the cart
    cart = Cart(request)
    #test for POST
    if request.POST.get('action') == 'post':
        #Get staff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        #look product in the DB
        product = get_object_or_404(Product, id=product_id)
        #sev to session
        cart.add(product=product, quantity=product_qty)

        # Get cart quantity
        cart_quantity = cart.__len__()

        #Return response
        # response = JsonResponse({'Product Name:' : product.name})
        response = JsonResponse({'qty:': cart_quantity})
        messages.success(request, 'product added successfully.')
        return response

def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        #Get staff
        product_id = int(request.POST.get('product_id'))
        #call delete function in cart
        cart.delete(product=product_id)

        response = JsonResponse({'product:': product_id})
        messages.success(request, 'Item deleted successfully...')
        return response
        # return redirect('cart_summary')





def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        #Get staff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        cart.update(product=product_id, quantity=product_qty)

        response = JsonResponse({'qty':product_qty})
        messages.success(request, 'Cart Updated successfully...')
        return response
        # return redirect('cart_summary')