from django.shortcuts import render,  redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
import datetime
from django.contrib import messages
from .models import calendario,uempaque,ucosecha,actual
from django.db.models import Avg, Count, Min, Sum
#from cosechas.models import diacosechas
from django.views.generic import ListView,CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.

def actualiza(request):
    anio_actual = datetime.date.today().year
    anio_inicio = anio_actual-5
    tupla_vacia=[anio_inicio]
    tupla_empaque=uempaque.objects.all()
    for i in range(anio_inicio+1, anio_actual+1):
       tupla_vacia.append(str(i))
   
    context = {'anexo':tupla_vacia,'anexo2':tupla_empaque}  
    return render(request, 'actual.html', context)

def grabaactual(request):
    estamos=actual.objects.filter(usuario=request.user)
    aqui=0
    aniog = request.POST['anio']
    semanag = request.POST['semana']
    calenda=calendario.objects.filter(semana=semanag,anio=aniog)
    if calenda.exists():

        if estamos.exists():
            for estaaqui in estamos:
                regis=estaaqui.id
                registro = actual.objects.get(pk=regis)
            
                registro.actual_anio=aniog
                registro.actual_semana=semanag

                mensaje="ACTUALIZANDO SUS FECHAS "
            
            registro.save()    
            
        else :
            arrastra= uempaque.objects.get(pk=1)
            arrasnome=arrastra.id
            nuevo_objeto = actual(actual_anio=aniog,actual_semana=semanag,
                                  usuario=request.user,empacadora=arrastra)
                
            nuevo_objeto.save()        

            mensaje="afectacion aplicada  "
            
    else :
            mensaje="NO APLICA CALENDARIO INEXISTENTE  " + str(aniog)
                
    context = {'mensaje':mensaje}
    return render(request, 'calendario.html', context)



def anios(request):
    anio_actual = datetime.date.today().year
    anio_inicio = anio_actual-5
    tupla_vacia=[anio_inicio]
   
    for i in range(anio_inicio+1, anio_actual+1):
       tupla_vacia.append(str(i))
   
    context = {'anexo':tupla_vacia}  
    return render(request, 'calendario.html', context)

def anios_crear(request,x):
    mymembers = calendario.objects.filter(anio=x).order_by('semana')
    
    context = {'eleccion':x,'mymembers':mymembers}
    return render(request,'crear_ca.html', context)

def crear_ca(request):
    

    #if request.GET['tope']:
        tope = request.GET['tope']
        topea = request.GET['topea']
        
        elecciona = request.GET['opciones']
        eleanio = request.GET['ANIO']
        ananio=int(eleanio)-1
        derecha = int(elecciona[-2:])
        colores=("blanca","amarilla","negra","roja","gris","verde","lila","cafe","naranja","azul")
        tupla_colores=[]
        for inicia in range(derecha-1,10):
             tupla_colores.append(colores[inicia])
        for completa in range(0,derecha-1):
             tupla_colores.append(colores[completa])
        inicio=0    
        ant=int(topea) 
        for actual in range(1,int(tope)+1):
            semana = actual
            anio = int(eleanio)
            color = tupla_colores[inicio]
            abueno=int(anio)
            inicio +=1
            if inicio==10:
                 inicio=0
            #print (str(anio),str(semana),color,str(abueno))  
            for atras in range(6,15):
                tiempo=actual-atras
                if atras==6:
                  if tiempo > 0:
                      ocho=tiempo
                      anio8=anio
                  else:
                      ocho=ant+tiempo
                     # print("ocho"+str(ocho)+str(tiempo))
                      anio8=ananio
                if atras==7:
                  if tiempo > 0:
                      nueve=tiempo
                      anio9=anio
                  else:
                      nueve=ant+tiempo
                     # print("nueve"+str(nueve)+str(tiempo))
                      anio9=ananio
                if atras==8:
                  if tiempo > 0:
                      diez=tiempo
                      anio10=anio
                  else:
                      diez=ant+tiempo
                     # print("diez"+str(diez)+str(tiempo))
                      anio10=ananio
                if atras==9:
                  if tiempo > 0:
                      once=tiempo
                      anio11=anio
                  else:
                      once=ant+tiempo
                     # print("once"+str(once)+str(tiempo))
                      anio11=ananio
                if atras==10:
                  if tiempo > 0:
                      doce=tiempo
                      anio12=anio
                  else:
                      doce=ant+tiempo
                     # print("doce"+str(doce)+str(tiempo))
                      anio12=ananio
                if atras==11:
                  if tiempo > 0:
                      trece=tiempo
                      anio13=anio
                  else:
                      trece=ant+tiempo
                     # print("trece"+str(trece)+str(tiempo))
                      anio13=ananio
                if atras==12:
                  if tiempo > 0:
                      catorce=tiempo
                      anio14=anio
                  else:
                      catorce=ant+tiempo
                     # print("catorce"+str(catorce)+str(tiempo))
                      anio14=ananio
                if atras==13:
                  if tiempo > 0:
                      quince=tiempo
                      anio15=anio
                  else:
                      quince=ant+tiempo
                     # print("quince"+str(quince)+str(tiempo))
                      anio15=ananio


            #print(ocho,anio8,nueve,anio9,diez,anio10)   
            grabaa=str(ocho)+str(anio8)
            grabab=str(nueve)+str(anio9)
            grabac=str(diez)+str(anio10)
            #print(once,anio11,doce,anio12,trece,anio13)  
            grabad=str(once)+str(anio11)
            grabae=str(doce)+str(anio12)
            grabaf=str(trece)+str(anio13)
            #print(catorce,anio14,quince,anio15)  
            grabag=str(catorce)+str(anio14)
            grabah=str(quince)+str(anio15)  
            graba1=anio
            graba2=semana
            graba3=str(semana)+str(anio)
            graba4=color

            nuevo_objeto = calendario(clave=anio,anio=graba1, semana=graba2,claveb=graba3,color=graba4,claveo=grabaa,claven=grabab,
                           claved=grabac,clavec=grabad ,clavee=grabae,clavet=grabaf,clavea=grabag,claveq=grabah  )
            
            nuevo_objeto.save()                             

        mensaje="afectacion aplicada  "
        return redirect('/anios/')
        #return HttpResponse(mensaje)   

def visual_ca(request):
     estamos=actual.objects.filter(usuario=request.user)
     for nines in estamos :
           ele=nines.actual_anio

     mymembers = calendario.objects.filter(anio=ele).order_by('semana')
         
     context = {'eleccion':ele,'mymembers':mymembers}
     return render(request,'visual_ca.html', context)      

    
def empacadoras(request):
  estamos=actual.objects.filter(usuario=request.user)
  for nines in estamos :
      empacadora=nines.empacadora.id

  if request.user.is_staff:
    # Allow access to internal dashboard
    empacadora=0

  mymembers = uempaque.objects.all()
  mycosechas = ucosecha.objects.all()
  #mymembers="santa fe,esmeralda,bondad,romina,cahua,lupita"
  
  template = loader.get_template('empacadoras_list.html')
  context = {
      'mymembers': mymembers,'actualizae':empacadora,'mycosechas':mycosechas
  }
  return HttpResponse(template.render(context, request))  

def empacadoraspro(request):
    
    mymembers="CATALOGO GENERAL DE EMPACADORAS "
    anexo2=""
    if request.method == 'POST':
        pass
        
    
    else :   
         mymembers2 = uempaque.objects.all().order_by('-id').values()[:5]
         anexo2=mymembers2
    context = {'anexo':mymembers,'anexo2':anexo2}      
    return render(request, 'agregauemp.html', context)

def grabauemp(request):
     if request.POST['nombre_ue']:
        nombreue=request.POST['nombre_ue']
        abreviaue=request.POST['abrevia_ue']
        #registro = uempaque.objects.get(pk=pk)
        nuevo_objeto = uempaque(nombre=nombreue,abreviatura=abreviaue)
        nuevo_objeto.save()    

        
        mymembers="CATALOGO GENERAL DE EMPACADORAS "
        mymembers2 = uempaque.objects.all().order_by('-id').values()[:5]
        anexo2=mymembers2
        messages.info(request, "Los DATOS DE LA UNIDAD EMPAQUE FUERON GRABADOS CORRECTAMENTE.")
     context = {'anexo':mymembers,'anexo2':anexo2}      
     return render(request, 'agregauemp.html', context)

def editauemp(request,pk):
    # if request.POST['nombre_ue']:
        registro = uempaque.objects.get(pk=pk)

        nombreue=registro.nombre
        abreviaue=registro.abreviatura
        
        print ('estamos adentro')
        mymembers="EDITANDO CATALOGO GENERAL DE EMPACADORAS "
        
        
        context = {'anexo':mymembers,'nombreue':nombreue,'abreviaue':abreviaue,'eleccion':pk}      
        return render(request, 'editauemp.html', context)

def activauemp(request,pk):
     registro = uempaque.objects.get(pk=pk)

     nombreue=registro.nombre
     abreviaue=registro.abreviatura
    # if request.POST['nombre_ue']:
     estamos=actual.objects.filter(usuario=request.user)
     if estamos.exists():
            for estaaqui in estamos:
                regis=estaaqui.id
                registro2 = actual.objects.get(pk=regis)
            
                registro2.empacadora=registro
                
            
            registro2.save()    
       
        
           
     mymembers="EDITANDO CATALOGO GENERAL DE EMPACADORAS "
        
        
     context = {'anexo':mymembers,'nombreue':nombreue,'abreviaue':abreviaue,'eleccion':pk}      
     return redirect('/empacadoras')

def updateuemp(request):
     if request.POST['nombre_ue']:
        nombreue=request.POST['nombre_ue']
        abreviaue=request.POST['abrevia_ue']
        elecc=request.POST['eleccion']
        registro = uempaque.objects.get(pk=int(elecc))
        
        registro.nombre=nombreue
        registro.abreviatura=abreviaue
        
        registro.save()    

        
        mymembers="CATALOGO GENERAL DE EMPACADORAS "
        mymembers2 = uempaque.objects.all().order_by('-id').values()[:5]
        anexo2=mymembers2
        
     context = {'anexo':mymembers,'anexo2':anexo2}      

     
     return redirect('/empacadoras')

def borrauemp(request,pk):
    # if request.POST['nombre_ue']:
        registro = uempaque.objects.get(pk=pk)

        registro.delete()
       
        mymembers="CATALOGO GENERAL DE EMPACADORAS "
        mymembers2 = uempaque.objects.all().order_by('-id').values()[:5]
        anexo2=mymembers2
        
        context = {'anexo':mymembers,'anexo2':anexo2}      

     
        return redirect('/empacadoras')

class ucosListView(ListView):
    model = ucosecha 

    def get_queryset(self):
        # Only allow deleting own articles
        if not self.request.user.is_superuser:
           return super().get_queryset().filter(usuario=self.request.user)
        else :
            return super().get_queryset().all()

class ucosCreateView(LoginRequiredMixin, CreateView):
    model = ucosecha
    fields = ["nombre",'abreviatura','empaque']
    success_url = reverse_lazy('basicos:cosechas')

    def form_valid(self, form):
        # Set the author before saving
        
        form.instance.usuario = self.request.user
        return super().form_valid(form)
        

class ucosUpdateView(LoginRequiredMixin, UpdateView):
    model = ucosecha
    fields = ["nombre",'abreviatura','empaque']

    def get_queryset(self):
        # Only allow editing own articles
        return super().get_queryset().filter(usuario=self.request.user)
    
    def get_success_url(self):
        # Redirect to the updated article
        return reverse_lazy('basicos:cosechas')
    



class ucosechaDeleteView(DeleteView):
    model = ucosecha
    

    def get_success_url(self):
        # Redirect to the updated article
        return reverse_lazy('basicos:cosechas')
    
def cosechado(request):
    estamos=actual.objects.filter(usuario=request.user)
    usa=request.user
    for nine in estamos:
        anio1=nine.actual_anio
        sema1=nine.actual_semana
    mymembers=ucosecha.objects.all()
    r8 = diacosechas.objects.values('uncosecha','usuario').filter(anio=anio1,
                                    semana=sema1).annotate(total_bolsas=Sum('bolsas')).order_by('-usuario')
    #print (r8)
    if request.user.is_superuser:
        return render(request, 'cosechados_userlist.html', {'rr8':r8,'mymembers':mymembers,'sema_asi':sema1,'estamos':usa})
    else :
        return render(request, 'cosechados_list.html', {'rr8':r8,'mymembers':mymembers,'sema_asi':sema1,'estamos':usa})


  
     
    
