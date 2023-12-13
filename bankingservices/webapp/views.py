from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def HomePage(request):
    return HttpResponse("<a href='/hi'>Hellow</a>")
def PyView(request):
    return HttpResponseRedirect(reverse('bye'))
def ByeView(request):
    return HttpResponse("Thanks for visiting")