#!/usr/bin/env python
# encoding: utf-8
#重新導入pattern函數用
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from restaurants.models import Restaurant, Comment
#date_time用的
from django.utils import timezone
from django.template import RequestContext
from restaurants.forms import CommentForm

def menu(request):
    """retrun a menu response

    :request: client request
    :returns: http response

    """
    path = request.path
    #先檢查request.GET有沒有id，若有則以get方法取得對應餐廳
    if 'id' in request.GET and request.GET['id'] != '':
    	restaurant = Restaurant.objects.get(id=request.GET['id'])
        return render_to_response('menu.html', locals())
    #若沒有則會讓頁面重導至pattern:/restaurants_list/
    else:
        return HttpResponseRedirect("/restaurants_list/")


def list_restaurants(request):
	restaurants = Restaurant.objects.all()
	return render_to_response('restaurants_list.html', locals())

def comment(request, restaurant_id):
    if restaurant_id:
        r = Restaurant.objects.get(id=restaurant_id)
    else:
        return HttpResponseRedirect("/restaurants_list/")
    errors = [] #用於作欄位正確性判斷
    if request.POST:
        visitor = request.POST['visitor']
        content = request.POST['content']
        email = request.POST['email']
        date_time = timezone.localtime(timezone.now())
        #當欄位未填，放入error(這時候error變False)
        if any(not request.POST[k] for k in request.POST):
            errors.append('* 有空白欄位，請不要留空')

        #檢驗email
        if '@' not in email:
            errors.append('* email格式有誤，請重新輸入')

        #若不是空白或檢驗無誤
        if not errors:
            Comment.objects.create(
                visitor=visitor, email=email,
                content=content,
                date_time=date_time,
                restaurant=r
            )
            #填寫成功將欄位清空
            visitor, email, content = ("","","")
    #產生一個非綁定表單，將生成html碼
    f = CommentForm()
    return render_to_response('comments.html', RequestContext(request,locals()))