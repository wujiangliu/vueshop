# -*- coding: utf-8 -*-

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from user_operation.models import UserFav

# 用户收藏，收藏数加 1
@receiver(post_save, sender=UserFav)
def create_user(sender, instance=None, created=False, **kwargs):
    if created:
        goods = instance.goods
        goods.fav_num += 1
        goods.save()

# 用户取消收藏，收藏数减 1
@receiver(post_delete, sender=UserFav)
def delete_user(sender, instance=None, created=False, **kwargs):
    goods = instance.goods
    goods.fav_num -= 1
    goods.save()