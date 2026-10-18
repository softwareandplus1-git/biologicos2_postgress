from django.shortcuts import render,redirect
from django.contrib.auth import login, logout, authenticate
from django.template import loader
from django.http import HttpResponse
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

def main(request):
  template = loader.get_template('main.html')
  string2=request.user
  string1 = "Hello World"
  request.session['nombreusu'] = 'NINGUNO'
  request.session['accesousu'] = 'NINGUNO'
  request.session['accesobod'] = 'NINGUNO'
  request.session['accesocos'] = 'NINGUNO'
             
  return HttpResponse(template.render())

def cerrar_sesion(request):
  logout(request)
  return redirect('main')

def logear(request):
  if request.method=="POST":
    form =AuthenticationForm(request,data = request.POST)
    if form.is_valid():
      nombre_usuario=form.cleaned_data.get("username")
      contra = form.cleaned_data.get("password")
      usuario=authenticate(username=nombre_usuario,password=contra)
      if usuario is not None:
      
        login(request, usuario)
        return redirect('main')
      else:
        messages.error(request,"usuario no valido")

    else:
      messages.error(request,"usuario no valido incorrecta")

  form = AuthenticationForm()
  return render(request,"login/login.html",{"form":form})

def registro_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('main') # Redirige al login o a la ruta deseada
    else:
        form = UserCreationForm()
        
    context = {'form': form}
    return render(request, 'registro.html', context)