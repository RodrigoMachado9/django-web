from django.shortcuts import render
from .models import Listing
from django.core.paginator import Paginator, EmptyPage


# Create your views here.


def index(request):
    # return render(request, 'listings/listings.jinja2', {
    #     'name': 'Machado'
    # })


    # listings = paginator_order_by('-list_date')     # fixme :)
    listings = paginator_order_by_with_filter('-list_date', is_published=True)  # fixme :)

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


### paginator -  filters


def paginator_order_by(order: str):
    # result data's in postgresql
    return Listing.objects.order_by(order)


def paginator_order_by_with_filter(order: str, **filters):
    # result data's in postgresql with filter
    data = Listing.objects.order_by(order).filter(**filters)
    return data
