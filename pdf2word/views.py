from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.conf import settings
from pdf2docx import Converter
from .forms import Pdf2wordForm


def home(request):
    if request.method == 'POST':
        form = Pdf2wordForm(request.POST, request.FILES)
        if form.is_valid():
            fs = FileSystemStorage()
            pdf_file = request.FILES['pdf_file']
            filename = pdf_file.name[:-3]
            pdf_file = fs.save(f'pdf2word-app\\pdfs\\{filename}.pdf', pdf_file)
            pdf_file_path = fs.path(pdf_file)
            # start convert
            cv = Converter(pdf_file_path)
            cv.convert(f'{settings.BASE_DIR}\\media\\pdf2word-app\\docxs\\{filename}.docx')
            cv.close()
            urls = [f"\\media\\pdf2word-app\\docxs\\{filename}.docx"]
            return render(request, 'thanks.html', context={'urls': urls})
        else:
            return render(request, 'pdf2word\\home.html', {'form': form})
    form = Pdf2wordForm()
    return render(request, 'pdf2word\\home.html', {'form': form})

