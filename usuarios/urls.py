from django.urls import path
from . import views 
from .views import usuListView,usuCreateView, usuUpdateView
#usuucosechaDeleteView, 


app_name = 'usuarios'

urlpatterns = [
    
     path("usuarios/", usuListView.as_view(),name="usuarios"),
     path("usuarios/add/", usuCreateView.as_view(), name="usuarios-add"),
     path("usuarios/<int:pk>/editar/", usuUpdateView.as_view(), name="author-update"),
          
#     path("cosechas/<int:pk>/borrar/", ucosechaDeleteView.as_view(), name="author-delete"),
#     path('cosechas/cosechado/', views.cosechado, name='cosechado'),
]
