from django.shortcuts import render

# Create your views here.

def MyTemView(request):
    return render(request,'MyApp/welcome.html')
