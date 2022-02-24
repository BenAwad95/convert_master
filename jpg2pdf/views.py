from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from PIL import Image
from .forms import JpgForm
# Create your views here.

def home(request):
    if request.method == 'POST':
        form = JpgForm(request.POST, request.FILES)
        image_jpg = request.FILES['image_jpg']
        fs = FileSystemStorage()
        jpg_file = fs.save(f'jpg2pdf-app/jpgs/{image_jpg.name}', image_jpg)
        jpg_file_path = fs.path(jpg_file)
        # start converting process
        jpg = Image.open(jpg_file_path)
        converted_pdf = jpg.convert('RGB')
        converted_pdf.save(f'{settings.BASE_DIR}\\media\\jpg2pdf-app\\pdfs\\{image_jpg.name[:-4]}.pdf')
        # return redirect(reverse_lazy('jpg2pdf:thanks'))
    form = JpgForm()
    return render(request, 'jpg2pdf/home.html', {'form': form})

def thanks(request):
    return HttpResponse('Thanks')