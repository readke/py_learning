from django.db import models

# Create your models here.

#城市
class country(models.Model):
    code = models.CharField(primary_key=True,max_length=10)
    country_name = models.CharField(max_length=100)

#商品
class goods(models.Model):
    code = models.CharField(primary_key=True,max_length=10)
    zh_name = models.CharField(max_length=100)
    en_name = models.CharField(max_length=100)

#企业注册地
class registration(models.Model):
    code = models.CharField(primary_key=True,max_length=10)
    name = models.CharField(max_length=100)

#贸易方式
class trade_type(models.Model):
    code = models.CharField(max_length=5)
    type_name = models.CharField(max_length=100)

#国家—商品
class goods_country(models.Model):
    rownum = models.IntegerField()
    month = models.CharField(max_length=20)
    country = models.CharField(max_length=255)
    goods = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    qty = models.BigIntegerField()
    flag = models.CharField(max_length=2)
    price_rmb = models.DecimalField(max_digits=16,decimal_places=2)
    price_dollar = models.DecimalField(max_digits=16,decimal_places=2)
    
    

    class Meta:
        unique_together = ("month","country","goods","flag")
    #primary =  ("month","country","goods","flag")