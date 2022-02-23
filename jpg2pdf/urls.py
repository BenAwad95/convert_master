from turtle import home
from django import views
from django.urls import path
from .views import home, thanks

app_name = 'jpg2pdf'
urlpatterns = [
    path('', home, name='home'),
    path('thanks/', thanks, name='thanks')
]
