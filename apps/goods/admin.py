from django.contrib import admin
from .models import Goods, GoodsImage, GoodsCategoryBrand, GoodsCategory
# Register your models here.

class GoodsCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category_type', 'parent_category', 'is_tab')

    list_editable = ('is_tab',)

    list_filter = ('category_type', 'is_tab')

class GoodsAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'category')
    list_filter = ('category',)

# 注册后台管理类
admin.site.register(Goods, GoodsAdmin)
admin.site.register(GoodsCategory, GoodsCategoryAdmin)
admin.site.register(GoodsCategoryBrand)
admin.site.register(GoodsImage)