from django.db import models
from django.utils.safestring import mark_safe
from django.utils.six import python_2_unicode_compatible

from system.storage import CustomFileStorage


@python_2_unicode_compatible
class Category(models.Model):  # 商品分类
    parent = models.ForeignKey('self', blank=True, null=True, verbose_name='上级分类(可不选)')
    name = models.CharField('分类名称', max_length=256)
    sort = models.IntegerField('排序')
    picture = models.ImageField('分类图片', upload_to='category/', default='category/default.jpeg',
                                storage=CustomFileStorage())

    def thumbnail(self):
        # 缩略图根据picture字段获取
        return mark_safe(u'<img src="%s" width="50px" />' % self.picture.url)

    # 页面显示的缩略图字段
    thumbnail.short_description = u'分类图片显示效果'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "商品分类"
        verbose_name_plural = "商品分类"


@python_2_unicode_compatible
class Goods(models.Model):  # 商品实体
    name = models.CharField('商品名称', max_length=64)
    price = models.FloatField('现价', max_length=8, default=0.0)
    old_price = models.FloatField('原价', max_length=8, default=0.0)
    created_time = models.DateTimeField('创建日期', auto_now_add=True)
    modified_time = models.DateTimeField('修改日期', auto_now=True)
    delete_flag = models.BooleanField('删除标记', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "商品"
        verbose_name_plural = "商品"
