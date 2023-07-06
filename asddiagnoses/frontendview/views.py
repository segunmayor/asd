from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    template = loader.get_template('pages/home.html')
    return HttpResponse(template.render())
    # return render(request, 'pages/home.html', {})

def diagnose(request):
    template = loader.get_template('pages/diagnose.html')
    return HttpResponse(template.render())