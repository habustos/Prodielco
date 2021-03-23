from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from .models import *


class Cliente_form(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('__all__')


class Transformador_form(forms.ModelForm):
    class Meta:
        model = Transformador
        fields = ('__all__')
        exclude = ('factor_correccion_k',)
        labels = {'tipo_transformador': 'Tipo Transformador',
                  'serial': 'Serial',
                  'referencia': 'Referencia',
                  'fecha_fabricacion': 'Fecha fabricacion',
                  'peso_kg': 'Peso Kg',
                  'litros_l': 'Litros Lt',
                  'tension_at': 'tension_at',
                  'tension_bt': 'tension_bt',
                  'potencia_kVA': 'Potencia kVA',
                  'temperatura': 'Temperatura',
                  'humedad': 'Humedad',
                  'medidor_De_Aislamiento': 'Medidor De Aislamiento',
                  'cliente': 'Cliente',
                  'clase_transformador': 'Clase Transformador',
                  'fabricante': 'fabricante',
                  'nomenclatura': 'nomenclatura',
                  'tap_nominal': 'tap_nominal',
                  'grupo_de_conexion': 'Grupo de conexión',
                  'departamento': 'Departamento',
                  'municipio': 'Municipio',
                  'barrio': 'Barrio',
                  'direccion': 'Direccion',
                  'email': 'Correo electronico'
                  }
        widgets = {
            #'fecha_fabricacion': forms.DateInput(format=('%Y'), attrs={'type': 'date'}),
            # 'depto': forms.TextInput(attrs={'class':'dropdown-item'}),
            # 'ciudad': forms.TextInput(attrs={'class':'dropdown-item'}),
        }


class R_aisl(forms.ModelForm):
    class Meta:
        model = Resistencia_aislamiento
        fields = ('__all__')
        exclude = ('prueba','categoria_prueba','tipo_prueba')


class Corr_20_ohm(forms.ModelForm):
    class Meta:
        model = Resistencia_aislamiento
        fields = ('__all__')
        exclude = ('prueba','categoria_prueba','tipo_prueba','cliente','transformador')

"""
class R_aisl_form(forms.ModelForm):
    class Meta:
        model = Resistencia_aislamiento
        EJECUCION = [('1', 'INICIAL'), ('2', 'FINAL')] #cambiar nombre ejecucion por prueba
        fields = ('__all__')
        prueba = forms.MultipleChoiceField(
            required=False,
            widget=forms.CheckboxSelectMultiple,
            choices=EJECUCION,
        )
        widgets = {
            #(attrs={'class':'dropdown-item'})
            # 'fecha_nacimiento': forms.DateInput(format=('%d-%m-%Y'), attrs={'type': 'date'}),
            # 'depto': forms.TextInput(attrs={'class':'dropdown-item'}),
            # 'ciudad': forms.TextInput(attrs={'class':'dropdown-item'}),
        }

"""
"""

class="mdb-select md-form" searchable="Search here.."
tipo_transformador = [
            ('seco', 'SECO'),
            ('lubricado', 'SUMERGIDO EN ACEITE'),
        ]

GEEKS_CHOICES =( 
    ("1", "One"), 
    ("2", "Two"), 
    ("3", "Three"), 
    ("4", "Four"), 
    ("5", "Five"), 
) 
  
# creating a form  
class GeeksForm(forms.Form): 
    geeks_field = forms.ChoiceField(choices = GEEKS_CHOICES)
    
    
        widgets = {
            'tipo_transformador': forms.ChoiceField(label=('tipo_transformador'),
                               choices=(('seco', ('SECO')),
                                        ('lubricado', ('SUMERGIDO EN ACEITE'))))
            #'fecha_documento': forms.DateInput(format=('%d-%m-%Y'), attrs={'type': 'date'}),
            #'fecha_nacimiento': forms.DateInput(format=('%d-%m-%Y'), attrs={'type': 'date'}),
            # 'depto': forms.TextInput(attrs={'class':'dropdown-item'}),
            # 'ciudad': forms.TextInput(attrs={'class':'dropdown-item'}),
        }"""