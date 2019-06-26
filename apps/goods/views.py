from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins, filters
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework_extensions.cache.mixins import CacheResponseMixin, RetrieveCacheResponseMixin, \
    ListCacheResponseMixin  # 缓存设置
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

from .serializers import CategorySerializer
from .serializers import GoodsSerializer
from .models import Goods, GoodsCategory
from .filters import GoodsFilter


# Create your views here.

class GoodsPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100

class GoodsListViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):

    """
    商品列表页，分页，过滤，搜索，排序
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    # authentication_classes = (TokenAuthentication, )
    # 限制ip访问速度
    throttle_classes = (UserRateThrottle, AnonRateThrottle)
    filter_class = GoodsFilter
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    # filter_fields = ('name', 'shop_price')
    search_fields = ('name', 'goods_brief', 'goods_desc')
    ordering_fields = ('shop_price', 'sold_num')


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        商品分类列表数据
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer

    # pagination_class = GoodsPagination

