from django.shortcuts import render
from .models import goods_country,goods
from django.http import HttpResponse,JsonResponse,HttpResponseForbidden
from django.core import serializers
from django.template import loader
from django.db.models import Sum
from django.db.models import F
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
def goodsCountryList(request):
    template = loader.get_template('goods/list.html')
    goods_list = goods.objects.values('code','zh_name','en_name')
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
        print(param)
        param = tuple(param) #列表转元组类型
        with connection.cursor() as cursor:
            cursor.execute(sql,param)
            rows = dictfetchall(cursor)
        
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