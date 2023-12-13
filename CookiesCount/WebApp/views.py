from django.shortcuts import render

# Create your views here.
def HitsView(request):
    hit = request.session.get('hit',0)
    newhit = hit+1
    request.session['hit'] = newhit
    return render(request,'MyApp/hits.html',{'hit':newhit})
