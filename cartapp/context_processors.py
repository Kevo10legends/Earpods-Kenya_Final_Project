

#Creating a context processor
def cart(request):
    from .cart import Cart
# Returning default data
    return {'cart': Cart(request)}
