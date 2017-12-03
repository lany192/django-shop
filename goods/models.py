from django.db import models
from django.utils import timezone
from django.utils.six import python_2_unicode_compatible

from system.storage import CustomFileStorage
from user.models import AppUser


@python_2_unicode_compatible
class Category(models.Model):  # 商品实体
    name = models.CharField('商品名称', max_length=64)
    nickname = models.CharField('昵称', max_length=64)
    birthday = models.DateField('生日', default=timezone.now)
    email = models.EmailField('邮箱', max_length=32)
    phone = models.CharField('电话', max_length=32)
    password = models.CharField('登录密码', max_length=64)
    avatar = models.ImageField('用户头像', upload_to='avatar/', default='avatar/user0.jpg', storage=CustomFileStorage())
    signature = models.CharField(max_length=128, default='这家伙很懒，什么也没留下.')
    created_time = models.DateTimeField('创建日期', default=timezone.now)
    modified_time = models.DateTimeField('最后修改日期', auto_now=True)
    delete_flag = models.BooleanField('删除标记', default=False)
    user = models.ForeignKey(AppUser)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Goods(models.Model):  # 商品实体
    name = models.CharField('商品名称', max_length=64)
    nickname = models.CharField('昵称', max_length=64)
    birthday = models.DateField('生日', default=timezone.now)
    email = models.EmailField('邮箱', max_length=32)
    phone = models.CharField('电话', max_length=32)
    password = models.CharField('登录密码', max_length=64)
    avatar = models.ImageField('用户头像', upload_to='avatar/', default='avatar/user0.jpg', storage=CustomFileStorage())
    signature = models.CharField(max_length=128, default='这家伙很懒，什么也没留下.')
    created_time = models.DateTimeField('创建日期', default=timezone.now)
    modified_time = models.DateTimeField('最后修改日期', auto_now=True)
    delete_flag = models.BooleanField('删除标记', default=False)
    user = models.ForeignKey(AppUser)

    def __str__(self):
        return self.name
