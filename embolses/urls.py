from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'embolses'

urlpatterns = [
      path('embolse/', views.embolse, name='embolse'),
      path('embolse/saldos/', views.saldosfruta, name='saldos'),
      path('saldosembolse/', views.embolse, name='saldosembolse'),
      path('embolse/listado/', views.listado, name='listado'),
      
    
   
    
   
    
    
    ]
