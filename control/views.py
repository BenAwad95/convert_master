from django.shortcuts import render

PROJECT_APPS = {
    'Jpg to Pdf': 'jpg2pdf',
    'Pdf to Jpg': 'pdf2jpg',
    'Word to Pdf': 'word2pdf',
    'Pdf to Word': 'pdf2word'
    }
def home(request):
    context = {
        'apps': PROJECT_APPS
    }
    return render(request, 'base.html', context)
