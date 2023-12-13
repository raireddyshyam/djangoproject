from django.shortcuts import render
from WebApp import forms
from django.http import HttpResponseRedirect
# Create your views here.
def thanks(request):
    return render(request,'MyApp/thanks.html')
def EmpView(request):
    if request.method == 'POST':
        form = forms.EmpForm(request.POST)
        if form.is_valid():
            print("Welcome to django Validations...")
            print(form.cleaned_data['Name'])
            print(form.cleaned_data['Sala'])
           # print(form.cleaned_data['FeedBack'])
            return HttpResponseRedirect('/thanks')
    else:
        form = forms.EmpForm()
    return render(request,'MyApp/welcome.html',{'form':form})
