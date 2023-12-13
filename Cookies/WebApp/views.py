from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def setcookie(request):
    response=HttpResponse("<h1>say hello welcome to cookie</h1>")
    response.set_cookie('user','sir')
    return response

def getcookie(request):
    user=request.COOKIES['user']
    return HttpResponse(user+'how are you...')

def deletecookie(request):
    response=HttpResponse("<h1>hello cookie deleted successfully</h1>")
    response.delete_cookie('user')
    return response