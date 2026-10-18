from django.urls import path
from . import views 
from .views import ucosListView,ucosCreateView, ucosechaDeleteView, ucosUpdateView



app_name = 'basicos'

urlpatterns = [
    
     path('anios/', views.anios, name='anios'),
     path('<int:x>/crear', views.anios_crear, name='crear_anios'),
     path('crearca/',views.crear_ca),
     path('visualca/',views.visual_ca),
     

     path('actual/',views.actualiza, name='actual'),
     path('grabaactual/',views.grabaactual, name='grabaactual'),

     path('usuactual/',views.usuactualiza, name='usuactual'),
     path('grabausuario/',views.grabausuario, name='grabausuario'),
     
     path('empacadoras/', views.empacadoras, name='empacadoras'),
     path('empacadoras/agrega/', views.empacadoraspro, name='agregaemp'),
     path('grabauemp/',views.grabauemp),
     path('updateuemp/',views.updateuemp),
     
     

     path('empacadoras/<int:pk>/editar', views.editauemp, name='editaemp'),
     path('empacadoras/<int:pk>/borrar', views.borrauemp, name='borraremp'),
     path('empacadoras/<int:pk>/activa', views.activauemp, name='activaemp'),

     path("cosechas/", ucosListView.as_view(),name="cosechas"),
     path("cosechas/add/", ucosCreateView.as_view(), name="author-add"),
     path("cosechas/<int:pk>/editar/", ucosUpdateView.as_view(), name="author-update"),
     path("cosechas/<int:pk>/borrar/", ucosechaDeleteView.as_view(), name="author-delete"),
     path('cosechas/cosechado/', views.cosechado, name='cosechado'),
]
