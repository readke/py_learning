from django.shortcuts import render
from .models import goods_country,goods
from django.http import HttpResponse,JsonResponse,HttpResponseForbidden
from django.core import serializers
from django.template import loader
from django.db.models import Sum
from django.db.models import F
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache
from django_redis import get_redis_connection
import logging

import json

logger = logging.getLogger(__name__)
conn = get_redis_connection("default") #获取原生redis客户端
# Create your views here.
def goodsCountryList(request):
    template = loader.get_template('goods/list.html')
    cache_key = "goods_type"
    goods_list = None
    if cache.has_key(cache_key):
        goods_list = cache.get(cache_key)
    else:
        goods_list = goods.objects.values('code','zh_name','en_name')
        cache.set(cache_key,goods_list,timeout=30*60)
        conn.expire(":1:"+cache_key,30*60)
    goods_list = list(goods_list)
    #print(goods_list)
    context = {'goods_list':goods_list}
    return HttpResponse(template.render(context, request))

@csrf_exempt
def ajaxGoodsCountryList(request):
    if request.method == 'GET':
        return HttpResponseForbidden
    #goods_country_list=goods_country.objects.values('country').annotate(sum_price=Sum('price_rmb')).annotate(name=F('country'), value=F('sum_price')).values('name', 'value')
    #goods_country_list = goods_country.objects.all()[:10]
    year = request.POST.get('year')
    flag = request.POST.get('flag')
    good_code = request.POST.get('good_code')
    print(year,flag,good_code)
    param = [] #定义一个列表类型用于接收请求查询参数
    try:
        
        rows = None
        cache_key = year+"_"+flag+"_"+good_code #缓存key
        if cache.has_key(cache_key):
            logger.info("从redis中取数据 ")
            print("从redis中取数据 ")
            #从缓存中取出数据
            #更新设置过期时间为30分钟
            rows = cache.get(cache_key)
            print(cache_key)
            conn.expire(":1:"+cache_key,30*60)
        else:
            logger.info("从数据库中取数据")
            print("从数据库中取数据")
            #从数据库中查询数据并放入缓存中，设置过期时间为30分钟
            sql = """ select gd.country_name as name,sum(gc.price_rmb) as value
                from goods_info_goods_country gc 
                left join goods_info_country gd on gc.country = gd.code """
            if flag:
                sql += " where gc.flag = %s "
                param.append(flag) #添加查询参数
            if year:
                sql += """ and substring(gc."month" from 1 for 4) =%s """
                param.append(year) #添加查询参数
            if good_code:
                sql += " and gc.goods =%s "
                param.append(good_code) #添加查询参数
            sql +=" GROUP BY gd.country_name ,gc.flag "
            #print(param)
            param = tuple(param) #列表转元组类型
            
            #执行sql
            with connection.cursor() as cursor:
                cursor.execute(sql,param)
                rows = dictfetchall(cursor)

            #将数据放入redis中
            cache.set(cache_key,rows,30*60)   
        
        datalist = list(rows)
    except Exception:
        print("序列化失败")
        return HttpResponse("序列化失败")
    else:
        return JsonResponse(datalist,safe=False)

def goodsList(request):
    return HttpResponse("good list")

def detail(request,code):
    return HttpResponse("detail")

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]