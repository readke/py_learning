from django.shortcuts import render

# Create your views here.

def index(request):
    '''学习笔记主页'''
    return render(request,'views/index.html')