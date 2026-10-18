from django.shortcuts import render
from django.views.generic import ListView,CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import diusuarios


# Create your views here.

class usuListView(ListView):
    model = diusuarios

    def get_queryset(self):
        # Only allow deleting own articles
        if not self.request.user.is_superuser:
           return super().get_queryset().all()
        else :
            return super().get_queryset().all()

class usuCreateView(LoginRequiredMixin, CreateView):
    model = diusuarios
    fields = ["nombre",'abreviatura','acceso']
    success_url = reverse_lazy('usuarios:usuarios')

    def form_valid(self, form):
        # Set the author before saving
        
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class usuUpdateView(LoginRequiredMixin, UpdateView):
    model = diusuarios
    fields = ["nombre",'abreviatura','acceso']

    def get_queryset(self):
        # Only allow editing own articles
        return super().get_queryset().all()
    
    def get_success_url(self):
        # Redirect to the updated article
        return reverse_lazy('usuarios:usuarios')
    
        
        



  
     
    

