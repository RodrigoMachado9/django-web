from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import Paginator, EmptyPage
from .choices import price, states, bedroom


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

    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        "listing": listing

    }

    return render(request, 'listings/listing.jinja2', context)


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # keywords
    if 'keywords' in request.GET:
        keywords = request.GET["keywords"]
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # city
    if 'city' in request.GET:
        city = request.GET["city"]
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)


    context = {
        "state_choice": states,
        "price_choice": price,
        "bedroom_choice": bedroom,
        "listings": queryset_list
    }

    return render(request, 'listings/search.jinja2', context)


### paginator -  filters

def paginator_order_by(order: str):
    # result data's in postgresql
    return Listing.objects.order_by(order)


def paginator_order_by_with_filter(order: str, **filters):
    # result data's in postgresql with filter
    data = Listing.objects.order_by(order).filter(**filters)
    return data
