from django.db import models
from django.contrib.auth.models import User
#from cajas.models import ucosecha
#from usuarios.models import diusuarios

# Create your models here.

class calidades(models.Model):
    nombre = models.CharField(max_length=25)
    abreviatura=models.CharField(max_length=12)
    peso_bruto=models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
            return self.nombre
      



# Create your models here.
