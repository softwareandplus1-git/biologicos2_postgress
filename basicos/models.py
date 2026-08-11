from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class calendario(models.Model):
  anio=models.IntegerField()
  semana=models.IntegerField()
  color=models.CharField(max_length=20)
  clave=models.IntegerField()
  claveb=models.CharField(max_length=6,default="")
  claveo=models.CharField(max_length=6,default="")
  claven=models.CharField(max_length=6,default="")
  claved=models.CharField(max_length=6,default="")
  clavec=models.CharField(max_length=6,default="")
  clavee=models.CharField(max_length=6,default="")
  clavet=models.CharField(max_length=6,default="")
  clavea=models.CharField(max_length=6,default="")
  claveq=models.CharField(max_length=6,default="")

class uempaque(models.Model):
  nombre=models.CharField(max_length=25)  
  abreviatura=models.CharField(max_length=12)

  def __str__(self):
        return self.nombre

class ucosecha(models.Model):
  nombre=models.CharField(max_length=25)
  abreviatura=models.CharField(max_length=12)
  usuario = models.ForeignKey(User,null='False',on_delete=models.CASCADE)
  empaque = models.ManyToManyField(uempaque)

  def __str__(self):
        return self.nombre
  
class actual(models.Model):
   actual_semana=models.IntegerField()
   actual_anio=models.IntegerField()
   usuario = models.OneToOneField(User, on_delete=models.CASCADE)
   fechaupdate=models.DateTimeField(auto_now=True)
   empacadora=models.ForeignKey(uempaque,null='False',on_delete=models.CASCADE)

  
  




  
  
