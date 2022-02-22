from django.urls import path
from. import views

app_name = 'word2pdf'
urlpatterns = [
    path('', views.home, name='home')
]
