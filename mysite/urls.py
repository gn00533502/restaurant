# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from views import here, math, welcome
#資料夾不同，from之位置亦不同
#list_restaurants為顯示餐廳列表模版
from restaurants.views import menu,list_restaurants, comment
#這個views指的是mysite/mysite/views.py


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^here/$', here),
    url(r'^(\d{1,2})/math/(\d{1,2})/$', math),
    url(r'^menu/$', menu),
    url(r'^welcome/$', welcome),
    url(r'^restaurants_list/$', list_restaurants),
    #提供一個參數:餐廳id，以顯示對應的餐廳評價
    url(r'^comment/(\d{1,5})/$', comment),
)
