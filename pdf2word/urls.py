from django.urls import path
from . import views

app_name = 'pdf2word'
urlpatterns = [
    path('', views.home, name='home')
]
