from django.shortcuts import render
from WebApp import forms
from django.http import HttpResponseRedirect
# Create your views here

def EmpView(request):
    if request.method == 'POST':
        form=forms.EmpForm(request.POST)
        if form.is_valid():
            print("Welcome to django validations...")
            print(form.cleaned_data['Nam'])
            print(form.cleaned_data['Job'])
            print(form.cleaned_data['Loc'])
            print(form.cleaned_data['Sal'])
            return HttpResponseRedirect('/Bad')
    else:
        form=forms.EmpForm()
    return render(request,'MyApps/welcome.html',{'form':form})
def Thanks(request):
    return render(request,'MyApps/Bad.html')