from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.six import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from system.storage import CustomFileStorage


@python_2_unicode_compatible
class UserProfile(models.Model):  # 系统用户的拓展实体
    user = models.OneToOneField(User, unique=True, verbose_name='用户')
    nickname = models.CharField('昵称', max_length=64)
    birthday = models.DateField('生日', default=timezone.now)
    email = models.EmailField('邮箱', max_length=32)
    phone = models.CharField('电话', max_length=32)
    avatar = models.ImageField('用户头像', upload_to='avatar/', default='avatar/user0.jpg', storage=CustomFileStorage())
    signature = models.CharField('个性签名', max_length=128, default='这家伙很懒，什么也没留下.')
    created_time = models.DateTimeField('创建日期', auto_now_add=True)
    modified_time = models.DateTimeField('修改日期', auto_now=True)

    def __str__(self):
        return self.nickname

    def __unicode__(self):
        return self.nickname

    class Meta:
        verbose_name = "用户其它信息"
        verbose_name_plural = "用户其它信息"


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = UserProfile()
        profile.user = instance
        profile.save()


post_save.connect(create_user_profile, sender=User)


@python_2_unicode_compatible
class AppToken(models.Model):  # app用户token实体
    user = models.OneToOneField(User, unique=True, verbose_name='用户')
    token = models.CharField('登录token', max_length=32)
    created_time = models.DateTimeField('创建日期', auto_now_add=True)
    overtime = models.DateTimeField('过期时间', auto_now=True)

    def __str__(self):
        return self.token

    class Meta:
        verbose_name = "登录信息"
        verbose_name_plural = "登录信息"
