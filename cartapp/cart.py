
from javaecomapp.models import Product

class Cart():
    def __init__(self, request):
        self.session = request.session

        #Get the current session key if it exists
        cart = self.session.get('session_key')
        #If user is new, create one
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        #make kart available to all pages
        self.cart = cart

    def add(self, product):
        product_id = str(product.id)
        # product_qty = str(quantity)

        #logic
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}
            # self.cart2[product_id] = int(product_qty)

        self.session.modified = True


    def __len__(self):
        return len(self.cart)

    def get_prods(self):
        #get ids from carts
        product_ids = self.cart.keys()
        #use ids to look products in the database
        products = Product.objects.filter(id__in=product_ids)
        #Retern the looked products
        return products
