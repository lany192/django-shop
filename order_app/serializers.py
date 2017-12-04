from django.contrib.auth.models import User, Group
from rest_framework import serializers

from blog.models import Category, Tag, Post

from order_app.models import Area, City, Province, Country, Address


# 地区
class AreaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Area
        fields = ('id', 'name', 'postcode')


# 城市
class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name', 'area', 'postcode')


# 省份
class ProvinceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Province
        fields = ('id', 'name', 'city')


# 国家
class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name', 'province')



# # 收货地址
# class AddressSerializer(serializers.HyperlinkedModelSerializer):
#     user = UserSerializer(many=True)
#     category = CategorySerializer()
#     author = AuthUserSerializer()
#
#     class Meta:
#         model = Address
#         fields = ('id', 'title', 'body', 'created_time', 'modified_time'
#                   , 'excerpt', 'views', 'category', 'tags', 'author')
