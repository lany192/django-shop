from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.six import python_2_unicode_compatible


@python_2_unicode_compatible
class User(models.Model):
    name = models.CharField('用户姓名', max_length=100)
    age = models.IntegerField('用户年龄', default=1)
    nickname = models.CharField('昵称', max_length=256)
    birthday = models.DateField('生日', default=timezone.now)
    created_time = models.DateTimeField('创建日期', default=timezone.now)
    modified_time = models.DateTimeField('最后修改日期', auto_now=True)


def __str__(self):
    return self.name
