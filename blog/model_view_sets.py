from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from blog.models import Category, Tag, Post
from blog.serializers import AuthUserSerializer, AuthGroupSerializer, CategorySerializer, TagSerializer, PostSerializer


# 系统用户
class AuthUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AuthUserSerializer


# 系统分组
class AuthGroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = AuthGroupSerializer


# 分类
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# 标签
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


# 文章
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('id')
    serializer_class = PostSerializer
