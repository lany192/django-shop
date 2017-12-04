# coding:utf-8
from django.contrib import admin

from goods_app.models import Goods, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'picture', 'parent']


class GoodsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'old_price']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Goods, GoodsAdmin)
