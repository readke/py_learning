from django.contrib import admin
from .models import goods_country,goods,country,registration,trade_type
# Register your models here.
admin.site.register(goods_country)
admin.site.register(goods)
admin.site.register(country)
admin.site.register(registration)
admin.site.register(trade_type)