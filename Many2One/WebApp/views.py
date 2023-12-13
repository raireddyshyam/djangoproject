from django.shortcuts import render
from .models import Team
# Create your views here.
def teamlist(request):
    items=Team.objects.all()
    return render(request,'MyApp/TeamPlayer.html',{'items':items})