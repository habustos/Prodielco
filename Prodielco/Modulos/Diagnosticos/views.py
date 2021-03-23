from django.views.generic import ListView, CreateView, UpdateView, View
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.shortcuts import render_to_response, HttpResponseRedirect
from django.template import RequestContext
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from openpyxl import Workbook
import pandas as pd
import numpy as np
import urllib.request, json
from datetime import datetime, timedelta
import sqlite3
from .models import *
from .forms import *





class add_buyer(CreateView):
    model = Cliente
    form_class = Cliente_form
    success_url = reverse_lazy('home')


class Transformador_form(CreateView):
    model = Transformador
    form_class = Transformador_form
    success_url = reverse_lazy('home')



def R_aisl_view(request):
    template_name = 'pruebas/R_aisl.html'

    if request.method == 'POST':
        R_aisl_form = R_aisl(request.POST)
        Corr_20_ohm_form = Corr_20_ohm(request.POST)

        if R_aisl_form.is_valid() and Corr_20_ohm_form.is_valid():
            R_aisl_form.save()
            Corr_20_ohm_form.save()
    else:
        R_aisl_form = R_aisl
        Corr_20_ohm_form = Corr_20_ohm
    return render(request,template_name, {
        'R_aisl_form': R_aisl_form,
        'Corr_20_ohm_form': Corr_20_ohm_form,
    })#, context_instance=RequestContext(request))



"""    
    return render_to_response(template_name, {
        'R_aisl_form': R_aisl_form,
        'Corr_20_ohm_form': Corr_20_ohm_form,
    }, context_instance=RequestContext(request))


class R_aisl_view(CreateView):
    R_aisl_form_class = R_aisl
    Corr_20_ohm_form_class = Corr_20_ohm
    template_name = 'pruebas/R_aisl.html'

    def resistencia(self, request):
        R_aisl_data = request.POST or None
        R_aisl_form = self.R_aisl_form_class(R_aisl_data, prefix='R_aisl')
        Corr_20_ohm_form = self.Corr_20_ohm_form_class(R_aisl_data, prefix='Corr_20_ohm')

        context = self.get_context_data(R_aisl_form=R_aisl_form,
                                        Corr_20_ohm_form=Corr_20_ohm_form)

        if R_aisl_form.is_valid():
            self.form_save(R_aisl_form)
        if Corr_20_ohm_form.is_valid():
            self.form_save(Corr_20_ohm_form)

        return self.render_to_response(context)

    def form_save(self, form):
        obj = form.save()
        messages.success(self.request, "{} saved successfully".format(obj))
        return obj

    def get(self, request, *args, **kwargs):
        return self.resistencia(request, *args, **kwargs)



class R_aisl_view(MultiModelFormView):
    template_name = 'pruebas/R_aisl.html'
    success_url = 'home'

    # here we specify all forms that should be displayed
    forms_classes = {
        'R_aisl_form' : R_aisl,
        'Corr_20_ohm_form' : Corr_20_ohm,
    }

    def get_forms_classes(self):
        forms_classes = super(R_aisl_view, self).get_forms_classes()
        user = self.request.user
        if not user.is_authenticated() or not user.is_staff:
            return list(filter(lambda form: not getattr(form, 'staff_only', False), forms_classes))
        return forms_classes

    def form_valid(self, form):
        print("yay it's valid!")
        return super(R_aisl_view).form_valid(form)




class R_aisl_view(CreateView):
    R_aisl_form_class = R_aisl
    Corr_20_ohm_form_class = Corr_20_ohm
    template_name = 'pruebas/R_aisl.html'

    def resistencia(self, request):
        R_aisl_data = request.POST or None
        R_aisl_form = self.R_aisl_form_class(R_aisl_data, prefix='R_aisl')
        Corr_20_ohm_form = self.Corr_20_ohm_form_class(R_aisl_data, prefix='Corr_20_ohm')

        context = self.get_context_data(R_aisl_form=R_aisl_form,
                                        Corr_20_ohm_form=Corr_20_ohm_form)

        if R_aisl_form.is_valid():
            self.form_save(R_aisl_form)
        if Corr_20_ohm_form.is_valid():
            self.form_save(Corr_20_ohm_form)

        return self.render_to_response(context)

    def form_save(self, form):
        obj = form.save()
        messages.success(self.request, "{} saved successfully".format(obj))
        return obj

    def get(self, request, *args, **kwargs):
        return self.resistencia(request, *args, **kwargs)
"""


"""
def multiple_forms(request):
    if request.method == 'POST':
        R_aisl_form = R_aisl(request.POST)
        Corr_20_ohm_form = Corr_20_ohm(request.POST)
        if R_aisl_form.is_valid() or Corr_20_ohm_form.is_valid():
            # Do the needful
            return render('pruebas/cliente.html')
    else:
        R_aisl_form = R_aisl()
        Corr_20_ohm_form = Corr_20_ohm()

    return render(request, 'pruebas/R_aisl.html', {
        'R_aisl_form': R_aisl_form,
        'Corr_20_ohm_form': Corr_20_ohm_form,
    }
                  )






class R_aisl_view(CreateView):
    model = Resistencia_aislamiento
    form_class = R_aisl
    success_url = reverse_lazy('home')


def R_aisl_view(request):
    #cliente = R_aisl_form.POST.get('selector-clientes')

    # cliente_id = self.kwargs['pk']
    # cliente_id = cliente.filter(cliente=cliente_id)
    if request.method == 'POST':
        form = R_aisl_form(request.POST)
        if form.is_valid():
            prueba = form.cleaned_data['field1']
            field2 = form.cleaned_data['field2']
            field3 = form.cleaned_data['field3']
            field4 = form.cleaned_data['field4']


            return render(request, 'pruebas/R_aisl.html',


                  {
                      'clientes': clientes,
                      'cliente': cliente,
                      'transformador':transformador,
                  }
                  )
        else:
            return render('pruebas/cliente.html')







def R_aisl_view(request):
    model = Resistencia_aislamiento
    form_class = R_aisl_form
    success_url = reverse_lazy('home')




    

        #if request.method=="POST"
        #    cliente =





class add_buyer(CreateView):

    form = Cliente_form(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()
            context = {
                'form': form,
                'personas': Cliente.objects.all()
            }
            return render(request, 'pruebas/cliente.html', context)

"""