import django_filters
from product.models import *
from home.models import Order_Product


class ProductFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        lookup_expr='icontains', label='')

    class Meta:
        model = Product
        fields = ['category', ]


class OrderFilter(django_filters.FilterSet):

    class Meta:
        model = Order_Product
        fields = ['status', ]
