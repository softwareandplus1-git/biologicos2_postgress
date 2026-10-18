from django.urls import path
from . import views 
from .views import cajListView,cajCreateView,cajUpdateView,cajDeleteView 


app_name = 'cajas'

urlpatterns = [
    
     path("cajas/", cajListView.as_view(),name="cajas"),
     path("cajas/add/", cajCreateView.as_view(), name="cajas-add"),
     path("cajas/<int:pk>/editar/", cajUpdateView.as_view(), name="cajas-update"),
     path("cajas/<int:pk>/borrar/", cajDeleteView.as_view(), name="author-delete"),
#     path('cosechas/cosechado/', views.cosechado, name='cosechado'),
]
