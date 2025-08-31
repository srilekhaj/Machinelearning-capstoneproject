from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
#from .forms import *
from django.contrib import messages
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,ListView,DetailView,CreateView,DeleteView,UpdateView)
from . import models
from .forms import *
from django.core.files.storage import FileSystemStorage

# ml imports

import time
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt

class dataUploadView(View):
    form_class = ckdForm
    success_url = reverse_lazy('success')
    template_name = 'create.html'
    failure_url= reverse_lazy('fail')
    filenot_url= reverse_lazy('filenot')
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    def post(self, request, *args, **kwargs):
        #print('inside post')
        form = self.form_class(request.POST, request.FILES)
        #print('inside form')
        if form.is_valid():
            form.save()
            data_age= request.POST.get('age')
            data_bmi=request.POST.get('bmi')
            data_child=request.POST.get('children')
            data_gender = request.POST.get('sex_male')
            data_smoke=request.POST.get('smoker_yes')
            data_reg=request.POST.get('region_southeast')
            #print (data)
            #dataset1=pd.read_csv("prep.csv",index_col=None)
            # dicc={'yes':1,'no':0} for classification result 
            filename = 'gb_model.sav'
            model = pickle.load(open(filename, 'rb'))
            # classifier = pickle.load(open(filename, 'rb'))

            data = np.array([data_age,data_bmi,data_child,data_gender,data_smoke,data_reg])
            
            #sc = StandardScaler()
            #data = sc.fit_transform(data.reshape(-1,1))
            # out=classifier.predict(data.reshape(1,-1))

            predicted_cost = model.predict(data.reshape(1,-1))[0]

# providing an index
            #ser = pd.DataFrame(data, index =['bgr','bu','sc','pcv','wbc'])

            #ss=ser.T.squeeze()
#data_for_prediction = X_test1.iloc[0,:].astype(float)

#data_for_prediction =obj.pca(np.array(data_for_prediction),y_test)
            #obj=ckd()
            ##plt.savefig("static/force_plot.png",dpi=150, bbox_inches='tight')







            return render(request, "succ_msg.html", {'data_age':data_age,'data_bmi':data_bmi,'data_child':data_child,
                                                     'data_gender':data_gender, 'data_smoke':data_smoke,
                                                     'data_reg':data_reg,'predicted_cost': round(predicted_cost, 2),
                                                     })


        else:
            return redirect(self.failure_url)

