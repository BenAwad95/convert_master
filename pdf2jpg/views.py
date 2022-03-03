from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from pdf2image import convert_from_path
from .forms import Pdf2jpgForm
# Create your views here.

def home(request):
    if request.method == 'POST':
        form = Pdf2jpgForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = request.FILES['pdf_file']
            filename = pdf_file.name[:-3]
            fs = FileSystemStorage()
            pdf_file = fs.save(f'pdf2jpg-app/pdfs/{filename}.pdf', pdf_file)
            pdf_file_path = fs.path(pdf_file)
            # start covert
            images = convert_from_path(pdf_file_path)
            count = 1
            urls = []
            for image in images:
                image.save(f'{settings.BASE_DIR}\\media\\pdf2jpg-app\\jpgs\\{filename}-{count}.jpg', 'JPEG')
                urls.append(f'\\media\\pdf2jpg-app\\jpgs\\{filename}-{count}.jpg')
                count+=1
            return render(request, 'pdf2jpg\home.html', {'form': form, 'done': True, 'urls': urls})
        else:
            return render(request, 'pdf2jpg\home.html', {'form': form})
    form = Pdf2jpgForm()
    return render(request, 'pdf2jpg\home.html', {'form': form})
