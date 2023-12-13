from django.shortcuts import render
from WebApp.models import FilterModel
# Create your views here.
def dataview(request):
    datalist=FilterModel.objects.all()
    return render(request,'MyApp/welcome.html',{'datalist':datalist})
def udataview(request):
    datalist=FilterModel.objects.all()
    return render(request,'MyApp/upper.html',{'datalist':datalist})
def dataview(request):
    datalist=FilterModel.objects.all()
    return render(request,'MyApp/lower.html',{'datalist':datalist})
def cdataview(request):
    datalist=FilterModel.objects.all()
    return render(request,'MyApp/ctf.html',{'datalist':datalist})