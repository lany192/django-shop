from django.contrib import admin

from comments.models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'text']


admin.site.register(Comment, CommentAdmin)
