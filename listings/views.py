from django.shortcuts import render
from .models import Listing

# Create your views here.


def index(request):
    return render(request, 'listings/listings.jinja2', {
        'name': 'Machado'
    })


def listing(request):
    return render(request, 'listings/listing.html')


def search(request):
    return render(request, 'listings/search.html')
