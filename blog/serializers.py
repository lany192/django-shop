from django.contrib.auth.models import User, Group
from rest_framework import serializers

from blog.models import Category, Tag, Post


# 系统用户
class AuthUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'groups')


# 系统分组
class AuthGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


# 分类
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'picture', 'created_time')


# 标签
class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'created_time')


# 文章
class PostSerializer(serializers.HyperlinkedModelSerializer):
    tags = TagSerializer(many=True)  # 数组
    category = CategorySerializer()  # 单个实体
    author = AuthUserSerializer()  # 单个实体

    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'created_time', 'modified_time'
                  , 'excerpt', 'views', 'category', 'tags', 'author')
