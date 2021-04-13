from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth, Group
from .forms import *
from .decorators import *
from product.models import *
from .filters import *
from .models import Seller
from .forms import *


def seller_signInPage(request):  # Signin views for seller

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')

    return render(request, 'seller_signin.html')


def seller_logoutPage(request):  # logout for seller
    logout(request)
    return redirect('seller_signin')


def seller_signUpPage(request):  # Signup views for seller

    mygroup = Group.objects.get(name='Seller')

    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('seller_signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('seller_signup')
            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.groups.add(mygroup)
                seller = Seller.objects.create(
                    user=user,
                    first_name=user.first_name,
                    last_name=user.last_name,
                    email=user.email,
                )
                seller.save()
                user.save()

                return redirect('seller_signin')

        else:
            messages.info(request, 'password not matching..')
            return redirect('seller_signup')
        return redirect('/')

    else:
        return render(request, 'seller_signup.html')


@login_required
@allowed_users(allowed_roles=['Seller'])
def seller_profilePage(request):  # Profile Page views for seller
    seller = request.user.seller
    form = SellerForm(instance=seller)

    if request.method == 'POST':
        form = SellerForm(request.POST, request.FILES, instance=seller)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'seller_profile.html', context)


@login_required(login_url='/seller_signin/')  # Dashboard for only seller
@allowed_users(allowed_roles=['Seller'])
def dashboard(request):
    return render(request, 'admin/dashboard.html')


@login_required(login_url='/seller_signin/')
@allowed_users(allowed_roles=['Seller'])
def productsView(request):
    product = Product.objects.all().filter(Seller=request.user.seller)
    search = ProductFilter(request.GET, queryset=product)
    product = search.qs
    context = {
        'product': product,
        'search': search,
    }
    return render(request, 'admin/products.html', context)


@login_required(login_url='/seller_signin/')
@allowed_users(allowed_roles=['Seller'])
def productDetailView(request, id):
    product = Product.objects.get(id=id)

    context = {
        'product': product,
    }
    return render(request, 'admin/product_detail.html', context)

# Product Create


@login_required(login_url='/seller_signin/')
@allowed_users(allowed_roles=['Seller'])
def categoryView(request):
    category = Category.objects.all().filter(Seller=request.user.seller)
    context = {'category': category}
    return render(request, 'admin/category.html', context)


@allowed_users(allowed_roles=['Seller'])
def category_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = CategoryForm()
        else:
            category = Category.objects.get(Seller=request.user.seller, id=id)
            form = CategoryForm(instance=category)
        return render(request, "admin/category_form.html", {'form': form})
    else:
        if id == 0:
            form = CategoryForm(request.POST)
        else:
            category = Category.objects.get(Seller=request.user.seller, id=id)
            form = CategoryForm(request.POST, instance=category)

        if form.is_valid():
            form.save()
        return redirect('category')


@allowed_users(allowed_roles=['Seller'])
def category_create(request):
    if request.method == "POST":
        category = request.POST.get('category')
        Category.objects.create(Seller=request.user.seller, category=category)
    return render(request, "admin/category_create.html")


@allowed_users(allowed_roles=['Seller'])
def category_delete(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect('category')


@login_required(login_url='/seller_signin/')
@allowed_users(allowed_roles=['Seller'])
def orderViewAdmin(request):

    orders = Order_Product.objects.all().filter(ordered=True)

    mFilter = OrderFilter(request.GET, queryset=orders)
    orders = mFilter.qs
    context = {
        'orders': orders,
        'mFilter': mFilter
    }

    return render(request, 'admin/orders.html', context)


def orderForm(request, id=id):

    if request.method == "GET":
        if id == 0:
            form = OrderStatusForm()
        else:
            order = Order_Product.objects.get(id=id)
            form = OrderStatusForm(instance=order)
        return render(request, "admin/order_form.html", {'form': form})
    else:
        if id == 0:
            form = OrderStatusForm(request.POST)
        else:
            order = Order_Product.objects.get(id=id)
            form = OrderStatusForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
        return redirect('orders')
