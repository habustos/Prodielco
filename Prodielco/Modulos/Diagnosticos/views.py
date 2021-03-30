from django.views.generic import ListView, CreateView, UpdateView, View
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import *
from .forms import *
import pandas as pd
import operator






class add_buyer(CreateView):
    model = Cliente
    form_class = Cliente_form
    success_url = reverse_lazy('home')


class Transformador_form(CreateView):
    model = Transformador
    form_class = Transformador_form
    success_url = reverse_lazy('home')


def R_aisl_view(request):
    ###Variables de prueba Inicial###
    temperatura = request.POST.get('temperatura')
    AT_BT_I_S_15 = request.POST.get('AT_BT_I_S_15')
    AT_BT_I_S_30 = request.POST.get('AT_BT_I_S_30')
    AT_BT_I_M_1 = request.POST.get('AT_BT_I_M_1')
    AT_BT_I_M_2 = request.POST.get('AT_BT_I_M_2')
    AT_BT_I_M_3 = request.POST.get('AT_BT_I_M_3')
    AT_BT_I_M_4 = request.POST.get('AT_BT_I_M_4')
    AT_BT_I_M_5 = request.POST.get('AT_BT_I_M_5')
    AT_BT_I_M_6 = request.POST.get('AT_BT_I_M_6')
    AT_BT_I_M_7 = request.POST.get('AT_BT_I_M_7')
    AT_BT_I_M_8 = request.POST.get('AT_BT_I_M_8')
    AT_BT_I_M_9 = request.POST.get('AT_BT_I_M_9')
    AT_BT_I_M_10 = request.POST.get('AT_BT_I_M_10')
    AT_T_I_S_15 = request.POST.get('AT_T_I_S_15')
    AT_T_I_S_30 = request.POST.get('AT_T_I_S_30')
    AT_T_I_M_1 = request.POST.get('AT_T_I_M_1')
    AT_T_I_M_2 = request.POST.get('AT_T_I_M_2')
    AT_T_I_M_3 = request.POST.get('AT_T_I_M_3')
    AT_T_I_M_4 = request.POST.get('AT_T_I_M_4')
    AT_T_I_M_5 = request.POST.get('AT_T_I_M_5')
    AT_T_I_M_6 = request.POST.get('AT_T_I_M_6')
    AT_T_I_M_7 = request.POST.get('AT_T_I_M_7')
    AT_T_I_M_8 = request.POST.get('AT_T_I_M_8')
    AT_T_I_M_9 = request.POST.get('AT_T_I_M_9')
    AT_T_I_M_10 = request.POST.get('AT_T_I_M_10')
    BT_T_I_S_15 = request.POST.get('BT_T_I_S_15')
    BT_T_I_S_30 = request.POST.get('BT_T_I_S_30')
    BT_T_I_M_1 = request.POST.get('BT_T_I_M_1')
    BT_T_I_M_2 = request.POST.get('BT_T_I_M_2')
    BT_T_I_M_3 = request.POST.get('BT_T_I_M_3')
    BT_T_I_M_4 = request.POST.get('BT_T_I_M_4')
    BT_T_I_M_5 = request.POST.get('BT_T_I_M_5')
    BT_T_I_M_6 = request.POST.get('BT_T_I_M_6')
    BT_T_I_M_7 = request.POST.get('BT_T_I_M_7')
    BT_T_I_M_8 = request.POST.get('BT_T_I_M_8')
    BT_T_I_M_9 = request.POST.get('BT_T_I_M_9')
    BT_T_I_M_10 = request.POST.get('BT_T_I_M_10')
    AT_BT_F_S_15 = request.POST.get('AT_BT_F_S_15')
    AT_BT_F_S_30 = request.POST.get('AT_BT_F_S_30')
    AT_BT_F_M_1 = request.POST.get('AT_BT_F_M_1')
    AT_BT_F_M_2 = request.POST.get('AT_BT_F_M_2')
    AT_BT_F_M_3 = request.POST.get('AT_BT_F_M_3')
    AT_BT_F_M_4 = request.POST.get('AT_BT_F_M_4')
    AT_BT_F_M_5 = request.POST.get('AT_BT_F_M_5')
    AT_BT_F_M_6 = request.POST.get('AT_BT_F_M_6')
    AT_BT_F_M_7 = request.POST.get('AT_BT_F_M_7')
    AT_BT_F_M_8 = request.POST.get('AT_BT_F_M_8')
    AT_BT_F_M_9 = request.POST.get('AT_BT_F_M_9')
    AT_BT_F_M_10 = request.POST.get('AT_BT_F_M_10')
    AT_T_F_S_15 = request.POST.get('AT_T_F_S_15')
    AT_T_F_S_30 = request.POST.get('AT_T_F_S_30')
    AT_T_F_M_1 = request.POST.get('AT_T_F_M_1')
    AT_T_F_M_2 = request.POST.get('AT_T_F_M_2')
    AT_T_F_M_3 = request.POST.get('AT_T_F_M_3')
    AT_T_F_M_4 = request.POST.get('AT_T_F_M_4')
    AT_T_F_M_5 = request.POST.get('AT_T_F_M_5')
    AT_T_F_M_6 = request.POST.get('AT_T_F_M_6')
    AT_T_F_M_7 = request.POST.get('AT_T_F_M_7')
    AT_T_F_M_8 = request.POST.get('AT_T_F_M_8')
    AT_T_F_M_9 = request.POST.get('AT_T_F_M_9')
    AT_T_F_M_10 = request.POST.get('AT_T_F_M_10')
    BT_T_F_S_15 = request.POST.get('BT_T_F_S_15')
    BT_T_F_S_30 = request.POST.get('BT_T_F_S_30')
    BT_T_F_M_1 = request.POST.get('BT_T_F_M_1')
    BT_T_F_M_2 = request.POST.get('BT_T_F_M_2')
    BT_T_F_M_3 = request.POST.get('BT_T_F_M_3')
    BT_T_F_M_4 = request.POST.get('BT_T_F_M_4')
    BT_T_F_M_5 = request.POST.get('BT_T_F_M_5')
    BT_T_F_M_6 = request.POST.get('BT_T_F_M_6')
    BT_T_F_M_7 = request.POST.get('BT_T_F_M_7')
    BT_T_F_M_8 = request.POST.get('BT_T_F_M_8')
    BT_T_F_M_9 = request.POST.get('BT_T_F_M_9')
    BT_T_F_M_10 = request.POST.get('BT_T_F_M_10')

    Resist_aisl = {
        "prueba":["INICIAL","INICIAL","INICIAL","FINAL","FINAL","FINAL"],
        "AT_BT_T": ["AT-BT","AT-T","BT-T","AT-BT","AT-T","BT-T"],
        "segundo_15": [AT_BT_I_S_15,AT_T_I_S_15,BT_T_I_S_15,AT_BT_F_S_15,AT_T_F_S_15,BT_T_F_S_15],
        "segundo_30": [AT_BT_I_S_30,AT_T_I_S_30,BT_T_I_S_30,AT_BT_F_S_30,AT_T_F_S_30,BT_T_F_S_30],
        "minuto_1": [AT_BT_I_M_1,AT_T_I_M_1,BT_T_I_M_1,AT_BT_F_M_1,AT_T_F_M_1,BT_T_F_M_1],
        "minuto_2": [AT_BT_I_M_2,AT_T_I_M_2,BT_T_I_M_2,AT_BT_F_M_2, AT_T_F_M_2, BT_T_F_M_2],
        "minuto_3": [AT_BT_I_M_3,AT_T_I_M_3,BT_T_I_M_3,AT_BT_F_M_3, AT_T_F_M_3, BT_T_F_M_3],
        "minuto_4": [AT_BT_I_M_4,AT_T_I_M_4,BT_T_I_M_4,AT_BT_F_M_4, AT_T_F_M_4, BT_T_F_M_4],
        "minuto_5": [AT_BT_I_M_5,AT_T_I_M_5,BT_T_I_M_5,AT_BT_F_M_5, AT_T_F_M_5, BT_T_F_M_5],
        "minuto_6": [AT_BT_I_M_6,AT_T_I_M_6,BT_T_I_M_6,AT_BT_F_M_6, AT_T_F_M_6, BT_T_F_M_6],
        "minuto_7": [AT_BT_I_M_7,AT_T_I_M_7,BT_T_I_M_7,AT_BT_F_M_7, AT_T_F_M_7, BT_T_F_M_7],
        "minuto_8": [AT_BT_I_M_8,AT_T_I_M_8,BT_T_I_M_8,AT_BT_F_M_8, AT_T_F_M_8, BT_T_F_M_8],
        "minuto_9": [AT_BT_I_M_9,AT_T_I_M_9,BT_T_I_M_9,AT_BT_F_M_9, AT_T_F_M_9, BT_T_F_M_9],
        "minuto_10": [AT_BT_I_M_10,AT_T_I_M_10,BT_T_I_M_10,AT_BT_F_M_10, AT_T_F_M_10, BT_T_F_M_10]
    }

###Variables de prueba final###
    if request.method == "POST":
        form = R_aisl(request.POST)
        Resist_aisl = pd.DataFrame(Resist_aisl)
        Resist_aisl["categoria_prueba_id"] = 1
        Resist_aisl["tipo_prueba_id"] = 1
        df_V_Correg_20_mohms = pd.DataFrame(Resist_aisl,
                                            columns=[
                                                'segundo_15',
                                                'segundo_30',
                                                'minuto_1',
                                                'minuto_2',
                                                'minuto_3',
                                                'minuto_4',
                                                'minuto_5',
                                                'minuto_6',
                                                'minuto_7',
                                                'minuto_8',
                                                'minuto_9',
                                                'minuto_10',
                                            ]
                                            ).astype(int)
        a, b = (0.5, (20 - float(temperatura)) / 10)
        df_V_Correg_20_mohms = operator.pow(a, b) * df_V_Correg_20_mohms
        df_i_absorcion = df_V_Correg_20_mohms['minuto_1'] / df_V_Correg_20_mohms['segundo_30']
        df_i_absorcion = round(df_i_absorcion, 1)
        df_i_absorcion= pd.DataFrame(df_i_absorcion)
        df_i_polaridad = df_V_Correg_20_mohms['minuto_10'] / df_V_Correg_20_mohms['minuto_1']
        df_i_polaridad = round(df_i_polaridad, 1)
        df_i_polaridad = pd.DataFrame(df_i_polaridad)
        df_polaridad_absorcion = pd.concat([df_i_absorcion,df_i_polaridad],axis=1)
        df_polaridad_absorcion.columns= ['indice_absorcion','indice_polaridad']
        df_V_Correg_20_mohms["categoria_prueba_id"] = 1
        df_V_Correg_20_mohms["tipo_prueba_id"] = 2
        df_AT_BT_T = pd.DataFrame(Resist_aisl, columns=['AT_BT_T'])
        df_prueba = pd.DataFrame(Resist_aisl, columns=['prueba'])
        df_V_Correg_20_mohms = pd.concat([df_prueba, df_AT_BT_T, df_V_Correg_20_mohms, df_polaridad_absorcion], axis=1)
        Resistencia_aislamiento = pd.concat([Resist_aisl, df_V_Correg_20_mohms], axis=0)
        print(Resistencia_aislamiento)


    else:
            return render(request, 'pruebas/R_aisl.html')
    return render(request,'pruebas/R_aisl.html',{'form': form})



"""

print(df_i_polaridad)
        print(df_i_absorcion)
        df_V_Correg_20_mohms["categoria_prueba_id"] = 1
        df_V_Correg_20_mohms["tipo_prueba_id"] = 2
        df_AT_BT_T = pd.DataFrame(Resist_aisl, columns=['AT_BT_T'])
        df_prueba = pd.DataFrame(Resist_aisl, columns=['prueba'])
        df_V_Correg_20_mohms = pd.concat([df_prueba,df_AT_BT_T, df_V_Correg_20_mohms, df_polaridad_absorcion], axis=1)
        print(df_V_Correg_20_mohms)
        Resistencia_aislamiento = pd.concat([Resist_aisl, df_V_Correg_20_mohms], axis=0)
        Resistencia_aislamiento.columns = ['ejecucion',
                                           'AT_BT_T', 'segundo_15', 'segundo_30', 'minuto_1', 'minuto_2',
                                           'minuto_3', 'minuto_4', 'minuto_5', 'minuto_6', 'minuto_7', 'minuto_8',
                                           'minuto_9', 'minuto_10', 'categoria_prueba_id', 'tipo_prueba_id',
                                           'indice_absorcion', 'indice_polaridad'
                                           ]

        #Resistencia_aislamiento.to_csv('df_V_Correg_20_mohms.csv')
        
        
        
        
        





class ProfileListView(ListView):
    template_name = 'pruebas/R_aisl_list.html'
    model = Resistencia_aislamiento


class ProfileFormView(MulT_IModelFormView):
    form_classes = {
        'avatar_form' : R_aisl,
        'background_form' : Corr_20_ohm,
        #'profile_form' : ProfileForm,
    }
    record_id = None
    template_name = 'pruebas/R_aisl.html'

    def get_form_kwargs(self):
        kwargs = super(ProfileFormView, self).get_form_kwargs()
        kwargs['avatar_form']['prefix'] = 'avatar'
        kwargs['background_form']['prefix'] = 'background'
        return kwargs

    def get_objects(self):
        self.Resistencia_aislamiento_id = self.kwargs.get('profile_id', None)
        try:
            profile = Resistencia_aislamiento.objects.get(id=self.Resistencia_aislamiento_id)
        except Resistencia_aislamiento.DoesNotExist:
            profile = None
        return {
            #'profile_form': profile,
            'R_aisl': profile.cliente if profile else None,
            'Corr_20_ohm': profile.transformador if profile else None,
        }

    def get_success_url(self):
        return reverse_lazy('profiles')

    def forms_valid(self, forms):
        profile = forms['profile_form'].save(commit=False)
        profile.avatar = forms['avatar_form'].save()
        profile.background = forms['background_form'].save()
        profile.save()
        return super(ProfileFormView, self).forms_valid(forms)





def R_aisl_view(request):
	context = {}
	Resistencia_aislamientoFomrset = modelformset_factory(Resistencia_aislamiento, form=R_aisl)
	form = Corr_20_ohm(request.POST or None)
	formset = Resistencia_aislamientoFomrset(request.POST or None, queryset= Resistencia_aislamiento.objects.none(),prefix='Resistencia_aislamiento')
	if request.method == "POST":
		if form.is_valid() and formset.is_valid():
			try:
				with transacT_Ion.atomic():
					student = form.save(commit=False)
					student.save()

					for mark in formset:
						data = mark.save(commit=False)
						data.student = student
						data.save()
			except IntegrityError:
				print("Error Encountered")

			return redirect('mulT_I_forms:list')


	context['formset'] = formset
	context['form'] = form
	return render(request, 'pruebas/cliente.html', context)

def list(request):
	datas = Resistencia_aislamiento.objects.all()
	return render(request, 'mulT_I_forms/list.html', {'datas':datas})





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



class R_aisl_view(MulT_IModelFormView):
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
        if not user.is_authenT_Icated() or not user.is_staff:
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



def mulT_Iple_forms(request):
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