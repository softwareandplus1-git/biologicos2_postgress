from django.db import models
from django.contrib.auth.models import User
from basicos.models import ucosecha
from usuarios.models import diusuarios

# Create your models here.

class embolses(models.Model):
  anio=models.IntegerField()
  semana=models.IntegerField()
  color=models.CharField(max_length=20)
  clave=models.CharField(max_length=6)
  usuario = models.ForeignKey(User,null='False',on_delete=models.CASCADE)
  fecha=models.DateField()
  bolsas=models.IntegerField()
  uncosecha=models.ForeignKey(ucosecha,on_delete=models.CASCADE)
  uncapturista=models.ForeignKey(diusuarios,null='False',on_delete=models.CASCADE)
 
  #class Meta:
        # Orden ascendente por nombre
        #ordering = ['uncosecha','anio','semana'] 
      


