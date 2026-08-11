from django.shortcuts import render,  redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
import datetime
from django.contrib import messages
from .models import embolses
from basicos.models import ucosecha,calendario,actual
from datetime import datetime, timedelta
from datetime import date
from django.views.generic import ListView,CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import OpcionForm
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count, Min, Sum



# Create your views here.
@login_required
def embolse(request):
    colorin=0
    coloriy=0
    valores_iniciales={'your_cantidad':0}
    form = OpcionForm(initial=valores_iniciales)
    
    actualiza=actual.objects.filter(usuario=request.user)
    for actualiza1 in actualiza:
        colorin=actualiza1.actual_semana
        coloriy=actualiza1.actual_anio

    
          

    ahora =  datetime.now()
    formato = "%Y-%m-%d"
    limiteii = ahora - timedelta(days=300)
    limitei = limiteii.strftime('%Y-%m-%d')
    limitef = ahora.strftime('%Y-%m-%d')
    limites = (ahora.strftime("%W")) # Número de semana (00-53)

    limitecolor=calendario.objects.filter(semana=limites)
    limitecolor=calendario.objects.filter(semana=colorin,anio=coloriy)
    
    for ami in limitecolor :
        colorasignado=ami.color

    


    if request.user.is_superuser:
         categorias = embolses.objects.filter(fecha__range=(limitei,limitef))
    else :    
         categorias = embolses.objects.filter(fecha__range=(limitei,limitef),usuario=request.user).order_by('uncosecha','semana')
      
     #mymembers2 = embolses.objects.all().order_by('-id').values()[:5]
    clave_usuario=str(coloriy)+str(colorin)
    if request.method == 'POST':
        form = OpcionForm(request.POST)
        nanio=form.data['your_ucosecha']
        
        nanie=ucosecha.objects.get(pk=nanio)
        
        
        if form.is_valid() :
           estamos = embolses.objects.filter(semana=colorin,anio=coloriy,uncosecha=nanie)
          
           if estamos.exists():
             for estaaqui in estamos:
                regis=estaaqui.id
                registro = embolses.objects.get(pk=regis)
            
                registro.fecha=ahora
                registro.bolsas=form.data['your_cantidad']
                registro.uncosecha=nanie
               
               
            
             registro.save() 
               
           else :
             nuevo_usuario = embolses.objects.create(anio=coloriy,
                        semana=colorin,
                        color=colorasignado,
                        clave=clave_usuario,
                        usuario=request.user,
                        fecha=ahora,
                        bolsas=form.data['your_cantidad'],
                        uncosecha=nanie
           )
           
          # nuevo_usuario.save()
           return redirect('/embolse/') 


           
    else :
        
        form = OpcionForm(request.POST or None, user=request.user,initial=valores_iniciales)
        #form = OpcionForm()
    
   
    #template = loader.get_template('embolses_list.html')
    #context = {
    #    'mymembers': categorias,'form':form
    #}
    #return HttpResponse(template.render(context, request))  
    return render(request, 'embolses_list.html', {'form': form,'mymembers':categorias,'asignado':colorasignado,'sema_asi':colorin,'sema_anio':coloriy})

def saldosfruta(request):
    colorin=0
    coloriy=0
    actualiza=actual.objects.filter(usuario=request.user)
    
    for actualiza1 in actualiza:
        colorin=actualiza1.actual_semana
        coloriy=actualiza1.actual_anio
        empaca_dora=actualiza1.empacadora
    edade2 = calendario.objects.filter(semana=colorin,anio=coloriy)
    for nameco in edade2:
         oc88 = nameco.claveo
         oc99 = nameco.claven
         oc10 = nameco.claved
         oc11 = nameco.clavec
         oc12 = nameco.clavee
         oc13 = nameco.clavet
         oc14 = nameco.clavea
         oc15 = nameco.claveq
    lista_colores=[]

    for ahorasi in range(8,16):
         if ahorasi==8:
            socho=(oc88.zfill(6)) #00123
         if ahorasi==9:
            socho=(oc99.zfill(6)) #00123
         if ahorasi==10:
            socho=(oc10.zfill(6)) #00123
         if ahorasi==11:
            socho=(oc11.zfill(6)) #00123
         if ahorasi==12:
            socho=(oc12.zfill(6)) #00123
         if ahorasi==13:
            socho=(oc13.zfill(6)) #00123    
         if ahorasi==14:
            socho=(oc14.zfill(6)) #00123
         if ahorasi==15:
            socho=(oc15.zfill(6)) #00123  

         sochook=int(socho[0:2])
         sochonk=int(socho[2:6])
         colocorrecto = calendario.objects.filter(semana=sochook,anio=sochonk)  
         for sisi in colocorrecto:    
              lista_colores.append(sisi.color)
         
    
    edades = calendario.objects.filter(semana=colorin,anio=coloriy)
    nombre_ucosecha8=[]
    bolsas_ucosecha8=[]
    nombre_ucosecha9=[]
    bolsas_ucosecha9=[]
    nombre_ucosecha10=[]
    bolsas_ucosecha10=[]
    nombre_ucosecha11=[]
    bolsas_ucosecha11=[]
    nombre_ucosecha12=[]
    bolsas_ucosecha12=[]
    nombre_ucosecha13=[]
    bolsas_ucosecha13=[]
    nombre_ucosecha14=[]
    bolsas_ucosecha14=[]
    nombre_ucosecha15=[]
    bolsas_ucosecha15=[]
    gran_total=[]
   
    for buedades in edades:
       
        for vltas in range(8,16):
            print (vltas)
            if vltas==8:
                       
                ocho = buedades.claveo
            if vltas==9:
                ocho = buedades.claven
                snueve=(ocho.zfill(6)) #00123

            if vltas==10:
                ocho = buedades.claved
                sdiez=(ocho.zfill(6)) #00123

            if vltas==11:    
                ocho = buedades.clavec
                sonce=(ocho.zfill(6)) #00123

            if vltas==12:
                ocho = buedades.clavee
                sdoce=(ocho.zfill(6)) #00123

            if vltas==13:
                 ocho = buedades.clavet
                 strece=(ocho.zfill(6)) #00123
            if vltas==14:
                ocho = buedades.clavea
                scatorce=(ocho.zfill(6)) #00123

            if vltas==15:
                 ocho = buedades.claveq
                 squince=(ocho.zfill(6)) #00123
                
                    
            socho=(ocho.zfill(6)) #00123
            sochook=int(socho[0:2])
            sochonk=int(socho[2:6])
            if request.user.is_superuser == True:
                estamos = embolses.objects.filter(semana=sochook,anio=sochonk).order_by('uncosecha','semana')
            
            else :
                    
              estamos = embolses.objects.filter(usuario=request.user,semana=sochook,anio=sochonk).order_by('uncosecha','semana')
            
           
            if estamos.exists():
                for datosem in estamos:
                   
                    status=1
                    
                    ochoca=datosem.bolsas
                    if vltas==8:
                       nombre_ucosecha8.append(datosem.uncosecha.id)
                       bolsas_ucosecha8.append(datosem.bolsas)
                    if vltas==9:
                       nombre_ucosecha9.append(datosem.uncosecha.id)
                       bolsas_ucosecha9.append(datosem.bolsas)   
                    if vltas==10:
                       nombre_ucosecha10.append(datosem.uncosecha.id)
                       bolsas_ucosecha10.append(datosem.bolsas)
                    if vltas==11:
                       nombre_ucosecha11.append(datosem.uncosecha.id)
                       bolsas_ucosecha11.append(datosem.bolsas)   
                    if vltas==12:
                       nombre_ucosecha12.append(datosem.uncosecha.id)
                       bolsas_ucosecha12.append(datosem.bolsas)
                    if vltas==13:
                       nombre_ucosecha13.append(datosem.uncosecha.id)
                       bolsas_ucosecha13.append(datosem.bolsas)   
                    if vltas==14:
                       nombre_ucosecha14.append(datosem.uncosecha.id)
                       bolsas_ucosecha14.append(datosem.bolsas)
                    if vltas==15:
                       nombre_ucosecha15.append(datosem.uncosecha.id)
                       bolsas_ucosecha15.append(datosem.bolsas)   
                   
            else :
                    ochoca=0
                    status=0
                    if request.user.is_superuser == True:
                       ninguna=ucosecha.objects.filter(empacadora=empaca_dora)
                     
                    else :   
                       ninguna=ucosecha.objects.filter(usuario=request.user)
                    if vltas==8:
                       for ninguno in ninguna:
                           nombre_ucosecha8.append(ninguno.id)
                           bolsas_ucosecha8.append(0)
                    if vltas==9:
                       for ninguno in ninguna:
                           nombre_ucosecha9.append(ninguno.id)
                           bolsas_ucosecha9.append(0)
                      # nombre_ucosecha9.append(datosem.uncosecha.id)
                      
                    if vltas==10:
                       for ninguno in ninguna:
                           nombre_ucosecha10.append(ninguno.id)
                           bolsas_ucosecha10.append(0)
                      # nombre_ucosecha10.append(datosem.uncosecha.id)
                      
                    if vltas==11:
                      # nombre_ucosecha11.append(datosem.uncosecha.id)
                      for ninguno in ninguna:
                           nombre_ucosecha11.append(ninguno.id)
                           bolsas_ucosecha11.append(0)
                       
                    if vltas==12:
                      # nombre_ucosecha12.append(datosem.uncosecha.id)
                      for ninguno in ninguna:
                           nombre_ucosecha12.append(ninguno.id)
                           bolsas_ucosecha12.append(0)
                       
                    if vltas==13:
                      # nombre_ucosecha13.append(datosem.uncosecha.id)
                      for ninguno in ninguna:
                           nombre_ucosecha13.append(ninguno.id)
                           bolsas_ucosecha13.append(0)
                          
                    if vltas==14:
                      # nombre_ucosecha14.append(datosem.uncosecha.id)
                      for ninguno in ninguna:
                           nombre_ucosecha14.append(ninguno.id)
                           bolsas_ucosecha14.append(0)
                       
                    if vltas==15:
                      # nombre_ucosecha15.append(datosem.id)
                      for ninguno in ninguna:
                           nombre_ucosecha15.append(ninguno.id)
                           bolsas_ucosecha15.append(0)
                     
                   

           
       
   
    
        
        
        
        
        
       
        
       

    
       
        nombreucosecha=[]
        bolsasucosecha=[]
        precios={}
        ochos={}
        nueves={}
        diezes={}
        onces={}
        doces={}
        treces={}
        catorces={}
        quinces={}
        if request.user.is_superuser == True:
             categorias=ucosecha.objects.filter(empaque=empaca_dora)
        else :
           categorias=ucosecha.objects.filter(usuario=request.user)

        for unidad in categorias:
            nombreucosecha.append(unidad.nombre)
           
            iden=unidad.id
            vlta=0
            for justo1 in nombre_ucosecha8:
                
                if iden==(justo1) :
                   bolsas8=str(bolsas_ucosecha8[vlta])
                   bolsas9=bolsas_ucosecha9[vlta]
                   bolsas10=bolsas_ucosecha10[vlta]
                   bolsas11=bolsas_ucosecha11[vlta]
                   bolsas12=bolsas_ucosecha12[vlta]
                   bolsas13=bolsas_ucosecha13[vlta]
                   bolsas14=bolsas_ucosecha14[vlta]
                   bolsas15=bolsas_ucosecha15[vlta]



                   bolsasucosecha.append(bolsas8)
                   bolsasucosecha.append(bolsas9)
                   bolsasucosecha.append(bolsas10)
                   bolsasucosecha.append(bolsas11)
                   bolsasucosecha.append(bolsas12)
                   bolsasucosecha.append(bolsas13)
                   bolsasucosecha.append(bolsas14)
                   bolsasucosecha.append(bolsas15)

                   precios[unidad.nombre]=unidad.nombre
                   ochos[unidad.nombre]=bolsas8
                   nueves[unidad.nombre]=bolsas9
                   diezes[unidad.nombre]=bolsas10
                   onces[unidad.nombre]=bolsas11
                   doces[unidad.nombre]=bolsas12
                   treces[unidad.nombre]=bolsas13
                   catorces[unidad.nombre]=bolsas14
                   quinces[unidad.nombre]=bolsas15
                   
                vlta=vlta+1       
            
                  
                   
                   
                
                  

       
        
    gran_tota=[]
    gran_vlta=0
    for key, value in ochos.items():  
      
       gran_vlta=gran_vlta+int(value)
    gran_tota.append(gran_vlta)
    gran_vlta=0
    for key, value in nueves.items():  
      
       gran_vlta=gran_vlta+int(value)
    gran_tota.append(gran_vlta)
    gran_vlta=0
    for key, value in diezes.items():  
      
       gran_vlta=gran_vlta+int(value)
    gran_tota.append(gran_vlta)
    gran_vlta=0
    for key, value in onces.items():  
      
       gran_vlta=gran_vlta+int(value)
    gran_tota.append(gran_vlta)
    gran_vlta=0
    for key, value in doces.items():  
      
       gran_vlta=gran_vlta+int(value)
    gran_tota.append(gran_vlta)
    gran_vlta=0
    for key, value in treces.items():  
      
       gran_vlta=gran_vlta+int(value)
    gran_tota.append(gran_vlta)
    gran_vlta=0
    for key, value in catorces.items():  
      
       gran_vlta=gran_vlta+int(value)
    gran_tota.append(gran_vlta)
    gran_vlta=0
    for key, value in quinces.items():  
      
       gran_vlta=gran_vlta+int(value)
    gran_tota.append(gran_vlta)



    if request.user.is_superuser == True:  
        total_paid = embolses.objects.filter(semana=sochook,anio=sochonk).aggregate(Sum('bolsas'))['bolsas__sum']
        result = embolses.objects.values('uncosecha').filter(semana=sochook,anio=sochonk).annotate(total_bolsas=Sum('bolsas'))
        #print (total_paid,'grupos',result)
            
    else :
            
    
       total_paid = embolses.objects.filter(usuario=request.user,semana=sochook,anio=sochonk).aggregate(Sum('bolsas'))['bolsas__sum']
       result = embolses.objects.values('uncosecha').filter(usuario=request.user,semana=sochook,anio=sochonk).annotate(total_bolsas=Sum('bolsas'))
    #print (total_paid,'grupos',result)
    
    
    lcle=['S08','S09','S10','S11','S12','S13','S14','S15']    
    mensaje="afectacion aplicada  "+str(colorin),str(coloriy)
    return render(request, 'saldos_list.html', {'mymembers':categorias,'sema_asi':colorin,
            'n8':nombre_ucosecha8,'c8':ochos,'c9':nueves,'c10':diezes,'c11':onces,'c12':doces,'c13':treces,
           'c14':catorces,'c15':quinces,'lcl':lista_colores,'lcl2':lcle,'lcl3':gran_tota})

def listado(request):
    mensaje="estamos en lista de embolses"
    colorin=0
    coloriy=0
   
    actualiza=actual.objects.filter(usuario=request.user)
    
    for actualiza1 in actualiza:
        colorin=actualiza1.actual_semana
        coloriy=actualiza1.actual_anio
    if not request.user.is_superuser:
       result = embolses.objects.values('uncosecha','semana').filter(usuario=request.user,anio=coloriy).annotate(total_bolsas=Sum('bolsas'))
    #print ('grupos',result)
       mymembers=ucosecha.objects.filter(usuario=request.user)   
    else :
       result = embolses.objects.values('uncosecha','semana').filter(anio=coloriy).annotate(total_bolsas=Sum('bolsas'))
  
      # mymembers=ucosecha.objects.all()   
       mymembers=ucosecha.objects.filter(usuario=request.user)   
  
    actualcintas=calendario.objects.filter(anio=coloriy)
    usuariosi=request.user
    context = {'mymembers':mymembers,'numeros':result,'semana_asi':colorin,'usuario_asi':usuariosi,'semanacolores':actualcintas,'resultado':result}      
    return render(request, 'listado_cintas.html', context)
     
   # return HttpResponse("Estás viendo la pregunta número")


