from django.shortcuts import render
from .models import Listing
from django.core.paginator import Paginator, EmptyPage


# Create your views here.


def index(request):
    # return render(request, 'listings/listings.jinja2', {
    #     'name': 'Machado'
    # })
    listings = Listing.objects.all()        # result data's in postgresql

    # added paginator...
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        "listings": paged_listings
    }

    return render(request, 'listings/listings.jinja2', context)


def listing(request, listing_id):
    print(listing_id)
    return render(request, 'listings/listing.html')


def search(request):
    return render(request, 'listings/search.html')
