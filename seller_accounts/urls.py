from django.urls import path
from .views import *

urlpatterns = [
    path('seller_signin/', seller_signInPage, name='seller_signin'),
    path('seller_logout/', seller_logoutPage, name='seller_logout'),
    path('seller_signup/', seller_signUpPage, name='seller_signup'),
    path('seller_profile/', seller_profilePage, name="seller_profile"),
    path('dashboard/', dashboard, name="dashboard"),
    path('products/', productsView, name="products"),
    # path('products-create/', productCreateView, name="products-create"),
    path('product_details/<id>',  productDetailView, name="product_details"),
    path('category/', categoryView, name="category"),
    path('category/<id>', category_delete, name="category_delete"),
    path('category_edit/<id>', category_form, name="category_edit"),
    path('category_add', category_create, name="category_add"),
    path('orders/', orderViewAdmin, name="orders"),
    path('order_update/<id>', orderForm, name="order_update"),
]
