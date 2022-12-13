from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

#import AI model
from . import aiModel

def upload(request):
    
    if request.method == 'POST' and request.FILES['upload']:
        upload = request.FILES['upload']
        fs = FileSystemStorage()
        print(upload.name)
        file = fs.save(upload.name, upload)
        print(file)
        file_url = fs.url(file)
        
        img_arr = aiModel.img_to_arr(upload.name)
        classification = aiModel.model.predict([img_arr])[0]
        
        return render(request, 'upload.html', {'file_url': file_url, 
        'class0': classification[0], 'class1': classification[1]})
        
    return render(request, 'upload.html')

def index(request):
    return render(request, 'index.html')

