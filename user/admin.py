from django.contrib import admin

# Register your models here.
from user.models import User, AppUser


class AppUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'nickname', 'email', 'birthday', 'phone', 'avatar', 'created_time', 'modified_time']
    list_per_page = 10
    search_fields = ['name', 'nickname', 'phone']
    list_editable = ['birthday', 'avatar']
    list_filter = ['created_time', ]
    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('id', 'name')


admin.site.register(AppUser, AppUserAdmin)
