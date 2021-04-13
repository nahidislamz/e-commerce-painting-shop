from django.contrib import admin
from .models import Cart, Order_Product, address
# Register your models here.
admin.site.register(Cart)
admin.site.register(Order_Product)
admin.site.register(address)
