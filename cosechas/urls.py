from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'diariocosechas'

urlpatterns = [
      path('diariocosechas/', views.dia_cosecha, name='dia_cosecha'),
      path('diariocosechas/saldos_cosecha/', views.saldosfruta2, name='saldos_cosecha'),
      path('diariocosechas/<int:pk>/borrar', views.borrarcdia, name='borrarcosechadia'),
    
   
    
   
    
    
    ]
