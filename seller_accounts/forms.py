from django import forms
from django.forms import ModelForm
from .models import Seller
from product.models import Product, Category
from home.models import Order_Product


class SellerForm(ModelForm):
    class Meta:
        model = Seller
        fields = '__all__'
        exclude = ['user']


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ['Seller']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('category',)
        labels = {
            'category': 'Category Name',
        }


class OrderStatusForm(forms.ModelForm):

    class Meta:
        model = Order_Product
        fields = ('status',)

    def __init__(self, *args, **kwargs):
        super(OrderStatusForm, self).__init__(*args, **kwargs)
        self.fields['status'].empty_label = "update status"
