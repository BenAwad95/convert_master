from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('Hello from word2pdf app')