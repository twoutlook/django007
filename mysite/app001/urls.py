from django.conf.urls import url

from . import views

app_name = 'app001'
urlpatterns = [
    url(r'^$', views.item000, name='index'),
    url(r'^spec/', views.spec, name='spec'),
    url(r'^cust/', views.cust, name='cust'),
    # https://docs.djangoproject.com/en/1.10/intro/tutorial03/
    #url(r'^item001/', views.item001, name='item001'), item001/123 後面有東西都好
    # url(r'^item001/$', views.item001, name='item001'), item001/123 後面不能有東西都好
    # …(?P<question_id>[0-9]+)
    
    url(r'^item001/(?P<item001_id>[_A-Za-z0-9-\\+]+)', views.item001detail, name='item001detail'), #item001/123 後面有東西都好
    url(r'^item001/$', views.item001, name='item001'), #item001/123 後面有東西都好
    
    # 在數據表沒有整合的情況下, 直接借 item001detail 來顯示單台機
    
    # url(r'^item003/(?P<item001_id>[_A-Za-z0-9-\#\\+]+)', views.item003detail, name='item003detail'), #item001/123 後面有東西都好
    
    #
    url(r'^item003v2/(?P<item001_id>[_A-Za-z0-9-\#\\+]+)', views.item003v2detail, name='item003v2detail'), #item001/123 後面有東西都好
    # url(r'^item003/$', views.item003, name='item003'),
    url(r'^item003v2/$', views.item003v2, name='item003v2'),
  
  
  
    # url(r'^item007/(?P<item001_id>[_A-Za-z0-9-\#\\+]+)', views.item007detail, name='item007detail'), #item001/123 後面有東西都好
    # url(r'^item007/$', views.item007, name='item007'),
  
  
    url(r'^item008/(?P<item001_id>[_A-Za-z0-9-\#\\+]+)', views.item008detail, name='item008detail'), #item001/123 後面有東西都好
    url(r'^item008/$', views.item008, name='item008'),
    
    url(r'^item009/(?P<item001_id>[_A-Za-z0-9-\#\\+]+)', views.item009detail, name='item009detail'), #item001/123 後面有東西都好
    url(r'^item009/$', views.item009, name='item009'),
    
    url(r'^item008blueprint/$', views.item008blueprint, name='item008blueprint'),
    url(r'^item009blueprint/$', views.item009blueprint, name='item009blueprint'),
  
  
  
    
    # url(r'^item002/', views.item002, name='item002'),
    # url(r'^item002a/', views.item002a, name='item002a'),
    
    # url(r'^item004/', views.item004, name='item004'),
    # url(r'^item004a/', views.item004a, name='item004a'),
    # url(r'^item004c/', views.item004c, name='item004c'),
    # url(r'^item004d/', views.item004d, name='item004d'),
    
    url(r'^item005/', views.item005, name='item005'),
    url(r'^item006/', views.item006, name='item006'),
    url(r'^dev001/', views.dev001, name='dev001'),
    url(r'^help/', views.help, name='help'),
    
    url(r'^index_bootstrap/', views.index_bootstrap, name='index_bootstrap'),
    url(r'^logout/', views.logout_view, name='logout_view'),
    
   
]