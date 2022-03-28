from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from docx2pdf import convert
from .forms import Word2pdfForm


def home(request):
    if request.method == 'POST':
        form = Word2pdfForm(request.POST, request.FILES)
        if form.is_valid():
            docx_file = request.FILES['docx_file']
            filename = docx_file.name[:-4]
            fs = FileSystemStorage()
            docx_file = fs.save(f'word2pdf-app/docxs/{filename}.docx', docx_file)
            docx_file_path = fs.path(docx_file)
            # start convert
            convert(docx_file_path, f'{settings.BASE_DIR}\\media\\word2pdf-app\\pdfs\\{filename}.pdf')
            urls = [f'\\media\\word2pdf-app\\pdfs\\{filename}.pdf']
            return render(request, 'thanks.html', context={'urls': urls})
        else:
            return render(request, 'word2pdf\home.html', {'form': form})
    form = Word2pdfForm()
    return render(request, 'word2pdf\home.html', {'form': form})

