from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

# Create your views here.


class HomePage(TemplateView):
    """
    Displays home page"
    """
    template_name = 'index.html'




