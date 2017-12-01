from django.contrib import admin

# Register your models here.
from user.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_time', 'modified_time', 'age', 'nickname', 'birthday']
    list_per_page = 10
    search_fields = ['name', ]
    list_editable = ['age', ]
    list_filter = ['created_time', ]
    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('id', 'name')


admin.site.register(User, UserAdmin)
