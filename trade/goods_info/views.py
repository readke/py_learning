from django.shortcuts import render
from .models import goods_country
from django.http import HttpResponse,JsonResponse
from django.core import serializers
from django.template import loader
import json
# Create your views here.
def goods_list(request):
    template = loader.get_template('goods/list.html')
    context = {}
    return HttpResponse(template.render(context, request))

def ajax_goods_list(request):
    goods_country_list = goods_country.objects.all()[:10]
    try:
        #response_data = {}
        response_data = serializers.serialize('json',goods_country_list)
    except Exception:
        print("序列化失败")
        return HttpResponse("序列化失败")
    else:
        return JsonResponse(response_data,safe=False)

def detail(request,code):
    return HttpResponse("detail")