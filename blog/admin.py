from django.contrib import admin
from .models import Post, Category, Tag

admin.site.site_header = "商品管理系统"
admin.site.site_title = "商品管理系统"


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_time', 'modified_time', 'category', 'author']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_time', 'modified_time', 'picture']
    list_per_page = 10
    search_fields = ['name', ]
    list_editable = ['picture', ]
    list_filter = ['created_time', ]
    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('id', 'name')


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag)
