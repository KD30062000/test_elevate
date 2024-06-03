from django.shortcuts import render
from django.http import HttpResponse
import os
from django.conf import settings

# Create your views here.
def index(request):
    return render(request,'index.html')
def download(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'Koushik_Das_Resume.pdf')  # Replace with your file path
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/octet-stream")
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
    return HttpResponse("File not found.")