from django.db import models

# Create your models here.

#城市
class country(models.Model):
    code = models.CharField(primary_key=True,max_length=10)
    county_name = models.CharField(max_length=100)

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
class goods_county(models.Model):
    rownum = models.IntegerField()
    month = models.IntegerField()
    country = models.ForeignKey(country,on_delete=models.CASCADE)
    goods = models.ForeignKey(goods,on_delete=models.CASCADE)
    unit = models.CharField(max_length=50)
    qty = models.BigIntegerField()
    flag = models.CharField(max_length=2)
    price_rmb = models.DecimalField(max_digits=10,decimal_places=2)
    price_dollar = models.DecimalField(max_digits=10,decimal_places=2)
    
    

    class Meta:
        unique_together = ("month","country","goods","flag")
    primary =  ("month","country","goods","flag")