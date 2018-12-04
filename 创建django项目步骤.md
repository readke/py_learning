# 一、创建Django项目

<font color=#0099ff  face="黑体">*带${}的项目是变量，自定义*</font>
## 1.  建立虚拟环境

    `python -m venv ${evn_name}`

---
## 2. 激活虚拟环境

    linux环境下： `source ${env_name}/bin/activate`

    windows环境下： `${env_name}\Scripts\activate`

---
## 3. 安装Django

    `pip install Django == ${Django_version} `

---
## 4. 在Django中创建项目

    `django-admin.py startproject ${project_name} .`

---
## 5. 启动应用

    `py manage.py runserver`

# 二、创建应用程序

## 1. 创建应用程序 

    `py manage.py startapp ${project_name_m}`

---
## 2. 定义模型

        from django.db import models

        class Pizza(models.Model):
            name = models.CharField(max_length=200)
            date_added = models.DateTimeField(auto_now_add=True)

            #显示类的相关信息
            def __str__(self):
                return self.name

---
## 3. 激活模型
    在settings.py中增加自己的应用
        
        INSTALLED_APPS = [
            --snip--
            'django.contrib.staticfiles',

            '${project_name_m}',
        ]

---
## 4. 修改数据库

     `py manage.py makemigrations ${project_name_m}`
     
     `py manage.py migrate`

---
## 5. 创建超级用户

    `py manage.py createsuperuser`

    输入超级用户名/email/密码，完成用户创建

---
## 6. 向管理网站注册模型

    在admin.py文件里注册我们创建的模型
        
        from django.contrib import admin

        from ${project_name_m}.models import Pizza

        admin.site.register(Pizza)

---
## 7. 启动应用

        py manage.py runserver

---
# 三、创建网页

## 1. 映射URL
    
    项目下的urls.py包括整个项目的url配置
    在应用下增加自己的 urls.py配置，然后在项目下的 urls.py中引用应用的 urls.py文件，实现模块化、分离管理

### 1.1 全局 pizzeria/pizzeria/urls.py 
        
        from django.conf.urls import url,include
        from django.contrib import admin

        urlpatterns = [
            url(r'^admin/', admin.site.urls),
            url(r'',include('pizzas.urls',namespace='pizzas')),
        ]
    
### 1.2 应用下的 pizzeria/pizzas/urls.py

        from django.conf.urls import url
        from . import views

        urlpatterns=[
            url(r'^$',views.index,name='index'),
        ]
---

## 2. 编写视图

在应用目录下的 view.py 添加视图

        from django.shortcuts import render

        # Create your views here.
        def index(request):
            return render(request,"views/index.html")

## 3. 编写模板

    




    
