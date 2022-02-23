from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .forms import JpgForm
# Create your views here.

def home(request):
    if request.method == 'POST':
        form = JpgForm(request.POST, request.FILES)
        # print(dir(form))
        # print(type(form.data['image_jpg']))
        print(type(request.FILES['image_jpg']))
        print(request.FILES['image_jpg'])
        # return redirect(reverse_lazy('jpg2pdf:thanks'))
    form = JpgForm()
    return render(request, 'jpg2pdf/home.html', {'form': form})

def thanks(request):
    # print(dir(request.FILES))
    # print(request.FILES)
    return HttpResponse('Thanks')