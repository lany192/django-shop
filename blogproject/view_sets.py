from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from blog.models import Category, Tag, Post
from blog.serializers import AuthUserSerializer, AuthGroupSerializer, CategorySerializer, TagSerializer, PostSerializer
from order_app.models import Area, City, Province, Country
from order_app.serializers import AreaSerializer, CitySerializer, ProvinceSerializer, CountrySerializer


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


# 地区
class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


# 城市
class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


# 省份
class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer


# 国家
class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
