from django.urls import path
from . import views

app_name = 'goods_info'
urlpatterns = [
    #ex:/polls/list
    
    path('list/',views.goodsCountryList,name='list'),
    path('ajaxList/',views.ajaxGoodsCountryList,name='ajaxList'),
    path('goodsList/',views.goodsList,name="goodsList"),
    path('<int:code>/',views.detail,name='detail'), 
   #3 path('list/',views.goods_list,name='list'),
    #path('list/',views.goods_list,name='list'),
    
    #ex:/polls/5/
    #path('<int:pk>/',views.DetailView.as_view(),name='detail'),
    #ex:/polls/5/results/
    #path('<int:pk>/results/',views.ResultsView.as_view(),name='results'),
    #ex:/polls/5/vote/
    #path('<int:question_id>/vote/',views.vote,name='vote'),
]