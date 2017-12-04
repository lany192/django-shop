# coding:utf-8
from django.contrib import admin

from order_app.models import Area, City, Province, Address, Order, Country


class AppTokenAdmin(admin.ModelAdmin):
    list_display = ['user', 'token', 'created_time', 'overtime']


class AreaAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'postcode']


class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'postcode']


class ProvinceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class CountryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'code']


class AddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'country', 'detail', 'consignee', 'phone']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'order_no', 'user', 'address', 'created_time']


admin.site.register(Area, AreaAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Province, ProvinceAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Order, OrderAdmin)
