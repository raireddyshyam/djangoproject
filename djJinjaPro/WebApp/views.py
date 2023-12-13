from django.shortcuts import render
import datetime
# Create your views here.
def DateView(request):
    dt=datetime.datetime.now()
    name="Front line Media"
    return render(request,'MyApp/welcome.html',{'dt':dt,'name':name})
