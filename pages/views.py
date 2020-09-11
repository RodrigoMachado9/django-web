from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.


def index(request):
    # return HttpResponse('<h1>Hello world</h1>')
    return render(request, 'pages/index.jinja2')


def about(request):
    return render(request, 'pages/about.jinja2')