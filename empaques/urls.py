from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'empaques'

urlpatterns = [
      path('empaques/', views.dia_empaque, name='dia_empaque'),
   #   path('diariocosechas/saldos_cosecha/', views.saldosfruta2, name='saldos_cosecha'),
   #   path('diariocosechas/<int:pk>/borrar', views.borrarcdia, name='borrarcosechadia'),
    #  path('diariocosechas/cosechas/', views.cosechas, name='cosechas'),
    #  path('empacadoras/<int:pk>/borrar', views.borrauemp, name='borraremp'),
      #path('saldosembolse/', views.embolse, name='saldosembolse'),
    
   
    
   
    
    
    ]
