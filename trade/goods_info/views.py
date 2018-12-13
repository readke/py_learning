from django.shortcuts import render
from .models import goods_country
from django.http import HttpResponse,JsonResponse
from django.core import serializers
from django.template import loader
from django.db.models import Sum
from django.db.models import F
from django.db import connection
import json
# Create your views here.
def goods_list(request):
    template = loader.get_template('goods/list.html')
    context = {}
    return HttpResponse(template.render(context, request))

def ajax_goods_list(request):
    #goods_country_list=goods_country.objects.values('country').annotate(sum_price=Sum('price_rmb')).annotate(name=F('country'), value=F('sum_price')).values('name', 'value')
    #goods_country_list = goods_country.objects.all()[:10]
    

    try:
        sql = """ select gd.country_name as name,sum(gc.price_rmb) as value
            from goods_info_goods_country gc 
            left join goods_info_country gd on gc.country = gd.code
            where flag = '1'
            GROUP BY gd.country_name ,gc.flag """
        with connection.cursor() as cursor:
            cursor.execute(sql)
            rows = dictfetchall(cursor)
        
        datalist = list(rows)
    except Exception:
        print("序列化失败")
        return HttpResponse("序列化失败")
    else:
        return JsonResponse(datalist,safe=False)

def detail(request,code):
    return HttpResponse("detail")

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]