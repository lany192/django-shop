from django.utils import timezone

from django.db import models
from django.utils.six import python_2_unicode_compatible

from goods_app.models import Goods
from user.models import UserProfile


@python_2_unicode_compatible
class Area(models.Model):  # 地区
    name = models.CharField('地区名称', max_length=64)
    postcode = models.IntegerField('邮编', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "地区"
        verbose_name_plural = "地区"


@python_2_unicode_compatible
class City(models.Model):  # 城市
    name = models.CharField('城市名称', max_length=64)
    area = models.ManyToManyField(Area, verbose_name="地区")
    postcode = models.IntegerField('邮编', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "城市"
        verbose_name_plural = "城市"


@python_2_unicode_compatible
class Province(models.Model):  # 省份
    name = models.CharField('省份名称', max_length=64)
    city = models.ManyToManyField(City, verbose_name="城市")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "省份"
        verbose_name_plural = "省份"


@python_2_unicode_compatible
class Country(models.Model):  # 国家
    name = models.CharField('国家/地区名称', max_length=64)
    code = models.IntegerField('国家/地区代码', default=0)
    province = models.ManyToManyField(Province, verbose_name="省份")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "国家"
        verbose_name_plural = "国家"


@python_2_unicode_compatible
class Address(models.Model):  # 收货地址
    user = models.OneToOneField(UserProfile, verbose_name='用户')
    country = models.OneToOneField(Country, verbose_name='国家')
    detail = models.CharField('详细地址', max_length=512)
    consignee = models.CharField('收件人', max_length=32)
    phone = models.CharField('电话', max_length=32)

    def __str__(self):
        return self.detail

    class Meta:
        verbose_name = "收货地址"
        verbose_name_plural = "收货地址"


@python_2_unicode_compatible
class Order(models.Model):  # 订单实体
    order_no = models.CharField('订单编号', max_length=64)
    goods_app = models.ManyToManyField(Goods, verbose_name='购买的商品')
    user = models.ForeignKey(UserProfile, verbose_name='下单用户')
    address = models.ForeignKey(Address, verbose_name='收货地址')
    created_time = models.DateTimeField('创建日期', auto_now_add=True)

    def __str__(self):
        return self.order_no

    class Meta:
        verbose_name = "订单"
        verbose_name_plural = "订单"
