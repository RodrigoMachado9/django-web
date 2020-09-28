from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact


# Create your views here.


def contact(requests):
    if requests.method == 'POST':
        listing_id = requests.POST['listing_id']
        listing = requests.POST['listing']
        name = requests.POST['name']
        email = requests.POST['email']
        phone = requests.POST['phone']
        message = requests.POST['message']
        user_id = requests.POST['user_id']
        realtor_email = requests.POST['realtor_email']

        # Check if user has made inquiry already
        if requests.user.is_authenticated:
            print("TESTE HERE", requests)

            user_id = requests.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(requests, 'You have already made an inquiry for this listing')
                return redirect('/listings/' + listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone,
                          message=message, user_id=user_id)

        contact.save()

        # Send email
        send_mail(
            'Property Listing Inquiry',
            'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info',
            'djangohelpservice@gmail.com',
            [realtor_email],
            fail_silently=False
        )

        messages.success(requests, 'Your request has been submitted, a realtor will get back to you soon')

        return redirect('/listings/' + listing_id)
