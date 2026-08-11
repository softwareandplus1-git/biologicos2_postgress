from django import forms
from basicos.models import ucosecha
from django.contrib.auth import authenticate




class OpcionForm(forms.Form):
    
    GEEKS_CHOICES = ucosecha.objects.all().values_list('id', 'nombre')
   # GEEKS_CHOICES = []
          


    #geeks_field = forms.ChoiceField(choices=GEEKS_CHOICES)
    #your_semana = forms.IntegerField(label="Semana ")
    your_cantidad = forms.IntegerField(label="Cantidad Encintado" )
    your_ucosecha = forms.ChoiceField(choices=GEEKS_CHOICES , label="Unidad de Cosecha") 
   
    def __init__(self, *args, **kwargs):
        
        user = kwargs.pop('user', None)
       
        super().__init__(*args, **kwargs)
       
        # Cambiar las opciones dinámicamente
        if user:
            #pass
            self.fields['your_ucosecha'].choices = ucosecha.objects.filter(usuario=user).values_list('id','nombre')
         
            
           

    

        
    


    
    
    
    
   

class MyCustomForm(forms.Form):
    # Standard field declaration
    my_field = forms.CharField()

    