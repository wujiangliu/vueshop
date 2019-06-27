# -*- coding: utf-8 -*-
"""vueshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework_jwt.views import obtain_jwt_token

import xadmin
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from vueshop.settings import MEDIA_ROOT
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from goods.views import GoodsListViewSet, CategoryViewSet
from users.views import UserViewSet
from user_operation.views import UserFavViewSet, AddressViewSet
from trade.views import ShoppingCartViewSet, OrderViewSet, AlipayView

router = DefaultRouter()
# 配置goods的url
router.register(r'goods', GoodsListViewSet, base_name='goods')
# 配置category的url
router.register(r'categorys', CategoryViewSet, base_name='categorys')
# 配置用户注册的url
router.register(r'users', UserViewSet, base_name='users')
# 配置用户收藏的url
router.register(r'userfavs', UserFavViewSet, base_name='userfav')
# 配置用户收藏的url
router.register(r'address', AddressViewSet, base_name='address')
# 购物车url
router.register(r'shopcarts', ShoppingCartViewSet, base_name='shopcarts')
# 订单管理url
router.register(r'orders', OrderViewSet, base_name='orders')
# 配置支付宝支付的url
# router.register(r'alipay/return', AlipayView.as_view(), base_name='alipay')


goods_list = GoodsListViewSet.as_view({'get': 'list'})
# category_list = CategoryViewSet.as_view({'get': 'list'})

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

    # 商品列表页
    url(r'^', include(router.urls)),
    # 商品分类
    # url(r'^category/', category_list, name='category'),
    # drf自带的token认证模式
    url(r'^api-token-auth/', views.obtain_auth_token),
    # jwt的认证接口
    url(r'^login/$', obtain_jwt_token),
    url(r'docs/', include_docs_urls(title='vueshop')),
    url(r'^alipay/return', AlipayView.as_view(), name='alipay'),
    # 第三方登录
    url('', include('social_django.urls', namespace='social'))
]
