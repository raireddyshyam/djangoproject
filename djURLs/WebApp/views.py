from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("<h1>Welcome to flm </h1>")
def index(request):
    return HttpResponse(f"Welcome to index page")