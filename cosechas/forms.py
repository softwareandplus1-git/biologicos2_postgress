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
         
            
           
class DiariocosechaForm(forms.Form):
    
    GEEKS_CHOICES = ucosecha.objects.all().values_list('id', 'nombre')
   
    GEEKS_DIAS = (
    ("1", "Domingo"),
    ("2", "Lunes"),
    ("3", "Martes"),
    ("4", "Miercoles"),
    ("5", "Jueves"),
    ("6", "Viernes"),
    ("7", "Sabado"),
)


          


    #geeks_field = forms.ChoiceField(choices=GEEKS_CHOICES)
    #your_semana = forms.IntegerField(label="Semana ")

    diassemana = forms.ChoiceField(choices=GEEKS_DIAS , label="Dia ") 
   
    your_cantidad8 = forms.IntegerField(label="  8 semanas" )
    
    your_cantidad9 = forms.IntegerField(label="  9 semanas" )

    your_cantidad10 = forms.IntegerField(label=" 10 semanas" )
    
    your_cantidad11 = forms.IntegerField(label=" 11 semanas" )

    your_cantidad12 = forms.IntegerField(label="  12 semanas" )
    
    your_cantidad13 = forms.IntegerField(label="  13 semanas" )

    your_cantidad14 = forms.IntegerField(label="  14 semanas" )
    
    your_cantidad15 = forms.IntegerField(label="  15 semanas" )

    your_ucosecha = forms.ChoiceField(choices=GEEKS_CHOICES , label="Unidad de Cosecha") 


   

    def __init__(self, *args, **kwargs):
        
        user = kwargs.pop('user', None)
        empacadora = kwargs.pop('empacadora', None)
        coli9 = kwargs.pop('coli9', None)
        
        super().__init__(*args, **kwargs)
       
        # Cambiar las opciones dinámicamente
        if user:
            #passArticle.objects.filter(publications__id=1)

            self.fields['your_ucosecha'].choices = ucosecha.objects.filter(empaque=empacadora).values_list('id','nombre')
            self.fields['your_cantidad8'].widget.attrs.update({'style': 'width: 160%;','class':"valor-dinamico"})
            self.fields['your_cantidad9'].widget.attrs.update({'style': 'width: 160%;','class':"valor-dinamico"})
            self.fields['your_cantidad10'].widget.attrs.update({'style': 'width: 160%;','class':"valor-dinamico"})
            self.fields['your_cantidad11'].widget.attrs.update({'style': 'width: 160%;','class':"valor-dinamico"})
            self.fields['your_cantidad12'].widget.attrs.update({'style': 'width: 160%;','class':"valor-dinamico"})
            self.fields['your_cantidad13'].widget.attrs.update({'style': 'width: 160%;','class':"valor-dinamico"})
            self.fields['your_cantidad14'].widget.attrs.update({'style': 'width: 160%;','class':"valor-dinamico"})
            self.fields['your_cantidad15'].widget.attrs.update({'style': 'width: 160%;','class':"valor-dinamico"})
            self.fields['your_ucosecha'].widget.attrs.update({'onchange':"myJavaScriptFunction()",'class':"clase-clic",'style': 'width: 260%;'})
    
            #self.fields['your_cantidad15'].widget.attrs['class'] = 'clase-clic'
            #self.fields['my_field'].widget.attrs['onclick'] = "myJavaScriptFunction()"
 
        # self.fields['my_field'].widget.attrs.update({'onclick': "myJavaScriptFunction()", 'class': "my-class"})
    


    
    
    
    
   

class MyCustomForm(forms.Form):
    # Standard field declaration
    my_field = forms.CharField()

    