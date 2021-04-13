from django import template
from home.models import Order_Product
register = template.Library()


@register.filter
def cart_count(user):
    order = Order_Product.objects.filter(user=user, ordered=False)
    if order.exists():
        return order[0].cartitem.count()
    else:
        return 0
