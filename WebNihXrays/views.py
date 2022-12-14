from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

#Import AI model - urls.py are run on server startup
from . import aiModel

def upload(request):
    
    if request.method == 'POST' and request.FILES['upload']:
        upload = request.FILES['upload']
        
        #Save image to show it later
        fs = FileSystemStorage()
        file = fs.save(upload.name, upload)
        file_url = fs.url(file)
        
        img_arr = aiModel.file_to_arr(upload)
        #There is one prediction in array
        classification = aiModel.model.predict([img_arr])[0]
        
        return render(request, 'upload.html', {'file_url': file_url, 
        'classification': classification})
        
    return render(request, 'upload.html')

def index(request):
    return render(request, 'index.html')

