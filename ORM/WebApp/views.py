from django.shortcuts import render
from WebApp.models import Student
# Create your views here.
def showdata(request):
    stds=Student.objects.filter(stdmarks__gte=40)
    print(type(stds))
    return render(request, 'MyApp/index.html', {'stds':stds})