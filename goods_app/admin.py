# coding:utf-8
from django.contrib import admin
from django.utils.safestring import mark_safe

from goods_app.models import Goods, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'thumbnail', 'parent']
    readonly_fields = ('thumbnail',)  # 必须加这行 否则访问编辑页面会报错


class GoodsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'old_price']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Goods, GoodsAdmin)
