from django.contrib import admin

from django.contrib import admin
from customerservice.models import *

class CityAdmin(admin.ModelAdmin):
    list_display = ['province', 'city_name']

class SchoolAdmin(admin.ModelAdmin):
    list_display = ['province', 'city_name']

class UserAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'nick_name', 'password', 'loginstate']



admin.site.register(School)
admin.site.register(TerminialType)
admin.site.register(Terminial)
admin.site.register(Printer)
admin.site.register(Wiscard)
admin.site.register(User,UserAdmin)
admin.site.register(Province)
admin.site.register(City,CityAdmin)
admin.site.register(Order)
admin.site.register(Status)
admin.site.register(OrderType)
admin.site.register(Classification)

