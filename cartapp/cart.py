from statistics import quantiles

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

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        #logic
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)

        self.session.modified = True



    def cart_total(self):
        #get product ids
        product_ids = self.cart.keys()
        #lookup those keys in products db models
        products = Product.objects.filter(id__in=product_ids)
        #get quantities
        quantitis = self.cart
        #start counting at zero
        total = 0
        for key, value in quantitis.items():
            #convert key string to int so we can do math
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.is_sale:
                        total = total + (product.sale_price * value)
                    else:
                        total = total + (product.sale_price * value)

        return total




    def __len__(self):
        return len(self.cart)

    def get_prods(self):
        #get ids from carts
        product_ids = self.cart.keys()
        #use ids to look products in the database
        products = Product.objects.filter(id__in=product_ids)
        #Retern the looked products
        return products

    def get_quants(self):
        quantities = self.cart
        return quantities

    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)

        #get cart
        ourcart = self.cart
        #Update Dictionary
        ourcart[product_id] = product_qty

        self.session.modified = True


        thing = self.cart
        return thing

    def delete(self, product):
        product_id = str(product)
        #delete from dectionary/cart
        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True