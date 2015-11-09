# encoding: utf-8

from django.contrib import admin
from restaurants.models import Restaurant, Food, Comment

#設定後台顯示餐廳的資料模式
class RestaurtAdmin(admin.ModelAdmin):
	list_display = ('name', 'phone_number', 'address')
	#搜尋功能
	search_fields = ('name',)
#設定後台的食物顯示資料模式
class FoodAdmin(admin.ModelAdmin):
	list_display = ('name', 'restaurant', 'price')
	#資料過濾與否模式
	list_filter = ('is_spicy',)
	search_fields = ('name',)
	#自定義編輯欄位，設定能編輯的欄位有哪些
	#fields = ('price','restaurant')
	#排序功能，由高到低
	ordering = ('-price',)

# Register your models here.
admin.site.register(Restaurant, RestaurtAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Comment)
