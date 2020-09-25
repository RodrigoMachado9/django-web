from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import Paginator, EmptyPage
from .choices import _price, _states, _bedroom


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

    ## todo - refactoring  this here  :*)

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

    # state
    if 'state' in request.GET:
        state = request.GET["state"]
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)  # fixme, attributes;

    # bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET["bedrooms"]
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)  # fixme, less than or equal

    # price
    if 'price' in request.GET:
        price = request.GET["price"]
        if price:
            queryset_list = queryset_list.filter(price__lte=price)  # fixme, less than or equal

    context = {
        "state_choice": _states,
        "price_choice": _price,
        "bedroom_choice": _bedroom,
        "listings": queryset_list,
        "values": request.GET
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
