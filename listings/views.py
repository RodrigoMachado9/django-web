from django.shortcuts import render
from .models import Listing
from django.core.paginator import Paginator, EmptyPage


# Create your views here.


def index(request):
    # return render(request, 'listings/listings.jinja2', {
    #     'name': 'Machado'
    # })

    # listings = Listing.objects.all()        # result data's in postgresql

    # listings = Listing.objects.order_by('-list_date')       # result data's in postgresql orderby

    listings = Listing.objects.order_by('-list_date').filter(is_published=True)       # result data's in postgresql with fiter

    # added paginator...
    paginator = Paginator(listings, 2)
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
