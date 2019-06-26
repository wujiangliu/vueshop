from django.contrib import admin
from .models import OrderInfo, OrderGoods, ShoppingCart
# Register your models here.

admin.site.register(ShoppingCart)
admin.site.register(OrderInfo)
admin.site.register(OrderGoods)