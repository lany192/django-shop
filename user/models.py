from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.six import python_2_unicode_compatible


@python_2_unicode_compatible
class User(models.Model):
    name = models.CharField('用户姓名', max_length=100)
    nickname = models.CharField('昵称', max_length=256)
    birthday = models.DateField('生日', default=timezone.now)
    email = models.EmailField('邮箱', max_length=32)
    phone = models.CharField('电话', max_length=32)

    created_time = models.DateTimeField('创建日期', default=timezone.now)
    modified_time = models.DateTimeField('最后修改日期', auto_now=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Account(models.Model):
    name = models.CharField('账号名称', max_length=100)
    pwd = models.CharField('登录密码', max_length=256)
    user = models.ForeignKey(User)
    token = models.CharField('登录token', max_length=32)
    created_time = models.DateTimeField('创建日期', default=timezone.now)
    overtime = models.DateTimeField('过期时间', auto_now=True)

    def __str__(self):
        return self.name
