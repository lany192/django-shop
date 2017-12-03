# coding:utf-8
from django.contrib import admin
from django.contrib.auth.models import User

from user.models import UserProfile


class ProfileInline(admin.StackedInline):  # 将UserProfile加入到Admin的user表中
    model = UserProfile
    verbose_name = '其它拓展属性'


class UserProfileAdmin(admin.ModelAdmin):
    inlines = (ProfileInline,)
    max_num = 1
    can_delete = False


admin.site.unregister(User)  # 去掉在admin中的注册
admin.site.register(User, UserProfileAdmin)  # 用userProfileAdmin注册user
