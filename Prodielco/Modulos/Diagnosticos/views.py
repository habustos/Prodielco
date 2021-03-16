from django.views.generic import ListView, CreateView, UpdateView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import *
from .forms import *
from .models import *


class add_buyer(CreateView):
    model = Cliente
    form_class = Cliente_form
    success_url = reverse_lazy('person_changelist')


"""
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