from django.shortcuts import render,redirect
from .models import Product, Offers, LatestBlog
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import SignUpForm, UpdateUserForm




def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)

        if user_form.is_valid():
            user_form.save()

            login(request, current_user)
            messages.success(request, 'Your account has been updated!')
            return redirect('index')
        return render(request, 'update_user.html', {'user_form': user_form})
    else:
        messages.success(request, 'You Must Be Logged In First!!!')
        return redirect('indexndex')






def search(request):
    #Determine if they filled out the form
    if request.method == "POST":
        searched = request.POST['searched']
        #Query the Products DB Model
        searched = Product.objects.filter(name__icontains=searched)
        # Test for null
        if not searched:
            messages.error(request, 'Sorry the product was not found!!! ..Try Again')
            return render(request, 'search.html', {})
        else:
            return render(request, 'search.html', {'searched': searched})
    else:
        return render(request, 'search.html', {})





def product(request,pk):
    product = Product.objects.get(id=pk)
    offers1 = Offers.objects.all()
    return render(request, 'product.html', {'product': product,
                                                                'offers1': offers1,})








# Create your views here.
def index(request):
    products = Product.objects.all()
    offers1 = Offers.objects.all()
    latestblog1 = LatestBlog.objects.all()
    # Fetch products for each category
    best_seller_products = Product.objects.filter(category__name="Best Seller")
    top_featured_products = Product.objects.filter(category__name="Top Featured")
    most_popular_products = Product.objects.filter(category__name="Most Popular")
    slider_products = Product.objects.filter(category__name="Sliders")

    # Pass the products to the template
    context = {
        'best_sellers': best_seller_products,
        'top_featured': top_featured_products,
        'most_popular': most_popular_products,
        'sliders': slider_products,
        'product': products,
        'offers1': offers1,
        'latestblog1': latestblog1,
    }

    return render(request, 'index.html', context)




def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request,'contact-us.html')



def checkout(request):
    return render(request,'checkout.html')

def gallery(request):
    product = Product.objects.all()
    return render(request,'gallery.html',{'products': product})

def my_account(request):
    return render(request,'my-account.html')

def shop(request):
    return render(request,'shop.html')

def shop2(request):
    return render(request,'shop-detail.html')

def wishlist(request):
    return render(request,'wishlist.html')

def base(request):
    return render(request,'base.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']

        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in successfully.')
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password. Try again.')
            return redirect('login')

    else:

        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('index')


def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # log in user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have Registered Successfully!!.')
            return redirect('index')
        else:
            messages.success(request, 'There was a problem Registering,Please try again!!?.')
            return redirect('register')
    else:
        return render(request, 'register.html', {'form': form})

