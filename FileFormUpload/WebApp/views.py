from django.shortcuts import render
from django.http import HttpResponseRedirect
from WebApp.forms import  StdForm
# Create your views here.
def home(request):
    return render(request,'MyApp/home.html')
def addnew(request):
    form = StdForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance=form.save()
        instance.save()
        return HttpResponseRedirect('/')
    context={'form':form}
    return render(request,'MyApp/stdadd.html',context)