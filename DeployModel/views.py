from django.http import HttpResponse
from django.shortcuts import render
import joblib
import numpy as np

def home(request):
    return render(request,"home.html")
   
def result(request):

    

    lis=[]
    lis.append(request.GET['hiddenq1'])
    lis.append(request.GET['hiddenq2'])
    lis.append(request.GET['hiddenq3'])
    lis.append(request.GET['hiddenq4'])
    lis.append(request.GET['hiddenq5'])
    lis.append(request.GET['hiddenq6'])
    lis.append(request.GET['hiddenq7'])
    lis.append(request.GET['hiddenq8'])
    lis.append(request.GET['hiddenq9'])
    lis.append(request.GET['hiddenq10'])
    lis.append(request.GET['age'])
    lis.append(request.GET['gender'])
    lis.append(request.GET['ethnicity'])
    lis.append(request.GET['hidden_jaun'])
    lis.append(request.GET['hidden_pdd'])
    lis.append(request.GET['country'])
    lis.append(request.GET['hidden_screen'])
    lis.append(request.GET['total_score_hidden'])
    lis.append(request.GET['who'])

    print(lis)

    tot=lis[17]

    loaded_model=joblib.load('model.pkl')

    arr=np.array(lis)
    nm=arr.reshape(1,19)
    a=loaded_model.predict(nm)


    return render(request,"result.html",{'ans':a,'total':tot})