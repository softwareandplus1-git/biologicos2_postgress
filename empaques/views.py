from django.shortcuts import render,  redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import render_to_string
from django.template import loader
import datetime
from django.contrib import messages
from .models import empaques
from basicos.models import ucosecha,calendario,actual
from embolses.models import embolses
from usuarios.models import diusuarios
from datetime import datetime, timedelta
from datetime import date
from django.views.generic import ListView,CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import DiarioempaqueForm
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count, Min, Sum
import os
#from xhtml2pdf import pisa
import io
from django.http import FileResponse, HttpResponseNotFound


# Create your views here.
@login_required
def dia_empaque(request):
   
    colorin=0
    coloriy=0
    valores_iniciales={'your_cantidad8':0,'your_cantidad9':0,'your_cantidad10':0,'your_cantidad11':0,
                       'your_cantidad12':0,'your_cantidad13':0,'your_cantidad14':0,'your_cantidad15':0}
    
    form = DiarioempaqueForm(initial=valores_iniciales)
    nombrecaptura=request.session['nombreusu'] 
    ucaptura=diusuarios.objects.filter(nombre=nombrecaptura)

    

    for ucap in ucaptura:
        claveusu=ucap.id
    
    
    actualiza=actual.objects.filter(usuario=request.user)
    for actualiza1 in actualiza:
        colorin=actualiza1.actual_semana
        coloriy=actualiza1.actual_anio
        colorie=actualiza1.empacadora

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
    lista_coloresa="----Dia de semana"
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
              lista_coloresa=lista_coloresa+" "+sisi.color.center(17,'-')
    lista_coloresa=lista_coloresa+"cargo a"
    
          

    ahora =  datetime.now()
    formato = "%Y-%m-%d"
    limiteii = ahora - timedelta(days=300)
    limitei = limiteii.strftime('%Y-%m-%d')
    limitef = ahora.strftime('%Y-%m-%d')
    limites = (ahora.strftime("%W")) # Número de semana (00-53)

    #limitecolor=calendario.objects.filter(semana=limites)
    limitecolor=calendario.objects.filter(semana=colorin,anio=coloriy)
    
    for ami in limitecolor :
        colorasignado=ami.color

    


    if request.user.is_superuser:
         categorias = empaques.objects.filter(fecha__range=(limitei,limitef))
    else :    
         categorias = empaques.objects.filter(semana=colorin,usuario=request.user).order_by('unempaque','semana')
      
     #mymembers2 = embolses.objects.all().order_by('-id').values()[:5]
    clave_usuario=str(coloriy)+str(colorin)
    if request.method == 'POST':
        form = DiarioempaqueForm(request.POST)
        nanio=form.data['your_ucosecha']
        nanie=ucosecha.objects.get(pk=nanio)
        claveuok=diusuarios.objects.get(pk=claveusu)
        diase=form.data['diassemana']
        #print (diase)
        #print(nanio,nanie)
        if form.is_valid():
          # estamos = diacosechas.objects.filter(semana=colorin,anio=coloriy,uncosecha=nanie)
                     estamos = diacosechas.objects.filter(usuario=request.user)
                         
                     nuevo_usuario = diacosechas.objects.create(anio=coloriy,
                        semana=colorin,
                        color=lista_coloresa[18:35],
                        clave=oc88,
                        usuario=request.user,
                        fecha=ahora,
                        bolsas=form.data['your_cantidad8'],
                        uncosecha=nanie,
                        diasemana=diase,
                        uncapturista=claveuok
                                     )
                        
                     nuevo_usuario = diacosechas.objects.create(anio=coloriy,
                        semana=colorin,
                        color=lista_coloresa[36:53],
                        clave=oc99,
       
                        usuario=request.user,
                        fecha=ahora,
                        bolsas=form.data['your_cantidad9'],
                        uncosecha=nanie,
                        diasemana=diase,
                        uncapturista=claveuok
                                          )
                                                

                     nuevo_usuario = diacosechas.objects.create(anio=coloriy,
                        semana=colorin,
                        color=lista_coloresa[54:71],
                        clave=oc10,
         
                        usuario=request.user,
                        fecha=ahora,
                        bolsas=form.data['your_cantidad10'],
                        uncosecha=nanie,
                        diasemana=diase,
                        uncapturista=claveuok
                                                 )
                                                
                     nuevo_usuario = diacosechas.objects.create(anio=coloriy,
                        semana=colorin,
                        color=lista_coloresa[72:89],
                        clave=oc11,
        
                        usuario=request.user,
                        fecha=ahora,
                        bolsas=form.data['your_cantidad11'],
                        uncosecha=nanie,
                        diasemana=diase,
                        uncapturista=claveuok
                                            )
                                                
                     nuevo_usuario = diacosechas.objects.create(anio=coloriy,
                        semana=colorin,
                        color=lista_coloresa[90:107],
                        clave=oc12,
                                 
   
                        usuario=request.user,
                        fecha=ahora,
                        bolsas=form.data['your_cantidad12'],
                        uncosecha=nanie,
                        diasemana=diase,uncapturista=claveuok
                                                 )
                                                
                        
                     nuevo_usuario = diacosechas.objects.create(anio=coloriy,
                        semana=colorin,
                        color=lista_coloresa[108:125],
                        clave=oc13,
                        usuario=request.user,
                        fecha=ahora,
                        bolsas=form.data['your_cantidad13'],
                        uncosecha=nanie,
                        diasemana=diase,
                        uncapturista=claveuok
                                               )
                                                
                     nuevo_usuario = diacosechas.objects.create(anio=coloriy,
                        semana=colorin,
                        color=lista_coloresa[126:143],
                        clave=oc14,
         

                        usuario=request.user,
                        fecha=ahora,
                        bolsas=form.data['your_cantidad14'],
                        uncosecha=nanie,
                        diasemana=diase,
                        uncapturista=claveuok
                                                 )
                                                
                     nuevo_usuario = diacosechas.objects.create(anio=coloriy,
                        semana=colorin,
                        color=lista_coloresa[144:161],
                        clave=oc15,
       
                        usuario=request.user,
                        fecha=ahora,
                        bolsas=form.data['your_cantidad15'],
                        uncosecha=nanie,
                        diasemana=diase,
                        uncapturista=claveuok
                                                 )
                                                
           
          # nuevo_usuario.save()
        return redirect('/diarioempaques/') 


           
    else :
        colores8='blanca'
        colores9='verde'
        form = DiarioempaqueForm(request.POST or None, empacadora=colorie,user=request.user,initial=valores_iniciales,coli9=colores9)
        #form = OpcionForm()
    
   
    #template = loader.get_template('embolses_list.html')
    #context = {
    #    'mymembers': categorias,'form':form
    #}
    #return HttpResponse(template.render(context, request))  
    
    return render(request, 'diaempaque_list.html', {'form': form,'mymembers':categorias,'asignado':colorasignado,
                            'listanombre':lista_coloresa,'blanca8':colores8, 'sema_asi':colorin,'sema_anio':coloriy})

def saldosfruta2(request):
    colorin=0
    coloriy=0
    actualiza=actual.objects.filter(usuario=request.user)
    
    for actualiza1 in actualiza:
        colorin=actualiza1.actual_semana
        coloriy=actualiza1.actual_anio
        quien = actualiza1.empacadora

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



          
        
    
    total_paid = embolses.objects.filter(usuario=request.user,semana=sochook,anio=sochonk).aggregate(Sum('bolsas'))['bolsas__sum']
    result = embolses.objects.values('uncosecha').filter(usuario=request.user,semana=sochook,anio=sochonk).annotate(total_bolsas=Sum('bolsas'))
    #print (total_paid,'grupos',result)
    

    #result8 = dia_cosecha.objects.values('uncosecha').filter(usuario=request.user,semana=sochook,
    #                                                      anio=sochonk).annotate(total_bolsas=Sum('bolsas'))
    
    ucosechas=ucosecha.objects.filter(usuario=request.user)
    #for nanis in ucosechas:
    #    ucos = nanis.id
    r8 = diacosechas.objects.values('clave','uncosecha').filter(clave=oc88,
                                                          anio=sochonk).annotate(total_bolsas=Sum('bolsas')).order_by('-clave')
    r9 = diacosechas.objects.values('clave','uncosecha').filter(clave=oc99,
                                                          anio=sochonk).annotate(total_bolsas=Sum('bolsas')).order_by('-clave')
    r10 = diacosechas.objects.values('clave','uncosecha').filter(clave=oc10,
                                                          anio=sochonk).annotate(total_bolsas=Sum('bolsas')).order_by('-clave')
    r11 = diacosechas.objects.values('clave','uncosecha').filter(clave=oc11,
                                                          anio=sochonk).annotate(total_bolsas=Sum('bolsas')).order_by('-clave')
    r12 = diacosechas.objects.values('clave','uncosecha').filter(clave=oc12,
                                                          anio=sochonk).annotate(total_bolsas=Sum('bolsas')).order_by('-clave')
    r13 = diacosechas.objects.values('clave','uncosecha').filter(clave=oc13,
                                                          anio=sochonk).annotate(total_bolsas=Sum('bolsas')).order_by('-clave')
    r14 = diacosechas.objects.values('clave','uncosecha').filter(clave=oc14,
                                                          anio=sochonk).annotate(total_bolsas=Sum('bolsas')).order_by('-clave')
    r15 = diacosechas.objects.values('clave','uncosecha').filter(clave=oc15,
                                                          anio=sochonk).annotate(total_bolsas=Sum('bolsas')).order_by('-clave')
   
   
    #    print (" ")
         #oc88 = nameco.claveo
         #oc99 = nameco.claven
         #oc10 = nameco.claved
         #oc11 = nameco.clavec
         #oc12 = nameco.clavee
         #oc13 = nameco.clavet
         #oc14 = nameco.clavea
         #oc15 = nameco.claveq
    saochos={}
    sanueves={}
    sadiezes={}
    saonces={}
    sadoces={}
    satreces={}
    sacatorces={}
    saquinces={}    
    print (r8)

    gran_cose=[]
    gran_sald=[]
    
    gran_vlta8=0
    gran_vlta9=0
    gran_vlta10=0
    gran_vlta11=0
    gran_vlta12=0
    gran_vlta13=0
    gran_vlta14=0
    gran_vlta15=0

   
    for fincas in categorias:
       
        for key in ochos :
            if fincas.nombre == key :
              
                embo=quinces[key]
                cose=0
                
                for edadquinces in r15 : 
                  
                    if fincas.id == edadquinces['uncosecha'] : 
                       cose = edadquinces['total_bolsas'] 
                       gran_vlta15=gran_vlta15+cose
   
                saquinces[fincas.nombre]=int(embo)-int(cose)
                
                embo=catorces[key]
                cose=0
                for edadcatorces in r14 : 
                  
                    if fincas.id == edadcatorces['uncosecha'] : 
                       cose = edadcatorces['total_bolsas'] 
                       gran_vlta14=gran_vlta14+cose
                sacatorces[fincas.nombre]=int(embo)-int(cose)

                embo=treces[key]
                cose=0
                for edadtreces in r13 : 
                  
                    if fincas.id == edadtreces['uncosecha'] : 
                       cose = edadtreces['total_bolsas'] 
                       gran_vlta13=gran_vlta13+cose
                satreces[fincas.nombre]=int(embo)-int(cose)

                embo=doces[key]
                cose=0
                for edaddoces in r12 : 
                  
                    if fincas.id == edaddoces['uncosecha'] : 
                       cose = edaddoces['total_bolsas'] 
                       gran_vlta12=gran_vlta12+cose
   
                sadoces[fincas.nombre]=int(embo)-int(cose)

                embo=onces[key]
                cose=0
                for edadonces in r11 : 
                  
                    if fincas.id == edadonces['uncosecha'] : 
                       cose = edadonces['total_bolsas'] 
                       gran_vlta11=gran_vlta11+cose
   
                saonces[fincas.nombre]=int(embo)-int(cose)

                embo=diezes[key]
                cose=0
                for edaddiezes in r10 : 
                  
                    if fincas.id == edaddiezes['uncosecha'] : 
                       cose = edaddiezes['total_bolsas'] 
                       gran_vlta10=gran_vlta10+cose
                sadiezes[fincas.nombre]=int(embo)-int(cose)

                embo=nueves[key]
                cose=0
                for edadnueves in r9 : 
                  
                    if fincas.id == edadnueves['uncosecha'] : 
                       cose = edadnueves['total_bolsas'] 
                       gran_vlta9=gran_vlta9+cose
                sanueves[fincas.nombre]=int(embo)-int(cose)

                embo=ochos[key]
                cose=0
                for edadochos in r8 : 
                  
                    if fincas.id == edadochos['uncosecha'] : 
                       cose = edadochos['total_bolsas'] 
                       gran_vlta8=gran_vlta8+cose
                saochos[fincas.nombre]=int(embo)-int(cose)
   
    gran_cose.append(gran_vlta8)
    gran_cose.append(gran_vlta9)
    gran_cose.append(gran_vlta10)
    gran_cose.append(gran_vlta11)
    gran_cose.append(gran_vlta12)
    gran_cose.append(gran_vlta13)
    gran_cose.append(gran_vlta14)
    gran_cose.append(gran_vlta15)
        
        

    #print (saquinces)   
    unido=1
    for hache in range(0,8):
        unida=1
        emb=gran_tota[hache]
        for hiche in range(0,8):
             if unido==unida:
                 cos=gran_cose[hiche]
                 sal=emb-cos
                 gran_sald.append(sal)
             unida=unida+1
        unido=unido+1        
        
        
    
    lcle=['S08','S09','S10','S11','S12','S13','S14','S15']    
    mensaje="afectacion aplicada  "+str(colorin),str(coloriy)

    

    



    return render(request, 'saldos_list.html', {'mymembers':categorias,'sema_asi':colorin,'rr8':r8,'rr9':r9,'rr10':r10,
           'n8':nombre_ucosecha8,'c8':ochos,'c9':nueves,'c10':diezes,'c11':onces,'c12':doces,'c13':treces,'rr11':r11,'rr12':r12,
           'c14':catorces,'c15':quinces,'lcl':lista_colores,'lcl2':lcle,'lcl3':gran_tota,'lcl4':gran_cose,'lcl5':gran_sald,'rr13':r13,'rr14':r14,
           'rr15':r15,'sas15':saquinces,'sas14':sacatorces,'sas13':satreces,'sas12':sadoces,'sas11':saonces,'sas10':sadiezes,'sas9':sanueves,'sas8':saochos})


def borrarcdia(request,pk):
    # if request.POST['nombre_ue']:
        registro = diacosechas.objects.get(pk=pk)

        registro.delete()
       
       
     
        return redirect('/diariocosechas')



