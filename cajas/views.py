from django.shortcuts import render
from django.views.generic import ListView,CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import calidades


# Create your views here.

class cajListView(ListView):
    model = calidades

    def get_queryset(self):
        # Only allow deleting own articles
        if not self.request.user.is_superuser:
           return super().get_queryset().all()
        else :
            return super().get_queryset().all()

class cajCreateView(LoginRequiredMixin, CreateView):
    model = calidades
    fields = ["nombre",'abreviatura','peso_bruto']
    success_url = reverse_lazy('cajas:cajas')

    def form_valid(self, form):
        # Set the author before saving
        
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class cajUpdateView(LoginRequiredMixin, UpdateView):
    model = calidades
    fields = ["nombre",'abreviatura','peso_bruto']

    def get_queryset(self):
        # Only allow editing own articles
        return super().get_queryset().all()
    
    def get_success_url(self):
        # Redirect to the updated article
        return reverse_lazy('cajas:cajas')
    
class cajDeleteView(DeleteView):
    model = calidades
    

    def get_success_url(self):
        # Redirect to the updated article
        return reverse_lazy('cajas:cajas')
        
        



  
     
    

