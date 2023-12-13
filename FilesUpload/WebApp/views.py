from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
# Create your views here.
def upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        print(myfile.name)
        print(myfile.size)
        fs = FileSystemStorage()
        filename = fs.save(myfile.name,myfile)
        uploadfile = fs.url(filename)
        return render(request,'MyApp/upload.html',{'uploadfile':uploadfile})
    return render(request,'MyApp/upload.html')
