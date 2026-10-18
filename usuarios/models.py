from django.db import models

# Create your models here.

class diusuarios(models.Model):
  class Acceso(models.TextChoices):
      BODEGA='B','Encintados'
      RAMPLA='R','Cosechados'
      AUDITOR='V','Consultas'
      
  nombre=models.CharField(max_length=25)
  abreviatura=models.CharField(max_length=12)
  acceso=models.CharField(max_length=1,choices=Acceso.choices,default=Acceso.AUDITOR,)
  
  
 

  def __str__(self):
        return self.nombre


