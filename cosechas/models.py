from django.db import models
from django.contrib.auth.models import User
from basicos.models import ucosecha
from usuarios.models import diusuarios

# Create your models here.

class diacosechas(models.Model):
    usuario=models.ForeignKey(User,null='False',on_delete=models.CASCADE)
    semana = models.IntegerField()
    anio = models.IntegerField()
    color=models.CharField(max_length=20)
    clave=models.CharField(max_length=6)
    fecha=models.DateField()
    bolsas=models.IntegerField()
    uncosecha=models.ForeignKey(ucosecha,on_delete=models.CASCADE)
    diasemana=models.CharField(max_length=15)
    uncapturista=models.ForeignKey(diusuarios,null='False',on_delete=models.CASCADE)
     

    class Meta:
        # Orden ascendente por nombre
        ordering = ['uncosecha','anio','semana'] 
      


