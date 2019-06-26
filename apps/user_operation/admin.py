from django.contrib import admin
from .models import UserFav, UserAddress, UserLeavingMessage
# Register your models here.

admin.site.register(UserAddress) # 收货地址
admin.site.register(UserFav) # 用户收藏
admin.site.register(UserLeavingMessage) # 用户留言