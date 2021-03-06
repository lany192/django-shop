# coding:utf-8
from django.contrib import admin
from django.contrib.auth.models import User

from user.models import UserProfile, AppToken


class ProfileInline(admin.StackedInline):  # 将UserProfile加入到Admin的user表中
    model = UserProfile
    verbose_name = '其它属性'


class UserProfileAdmin(admin.ModelAdmin):
    inlines = (ProfileInline,)
    max_num = 1
    can_delete = False


class AppTokenAdmin(admin.ModelAdmin):
    list_display = ['user', 'token', 'created_time', 'overtime']


admin.site.unregister(User)  # 去掉在admin中的注册
admin.site.register(User, UserProfileAdmin)  # 用userProfileAdmin注册user
admin.site.register(AppToken, AppTokenAdmin)
