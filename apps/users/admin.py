from django.contrib import admin
from .models import UserProfile, VerifyCode
# Register your models here.

admin.site.register(UserProfile) # 用户信息
admin.site.register(VerifyCode) # 短信验证码
