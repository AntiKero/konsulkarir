from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact
from listings.models import Listing
from django.contrib.auth.models import User

def contact(request):
  if request.method == 'POST':
    listing_no = request.POST['listing_id']
    listing_id = Listing.objects.get(id=request.POST['listing_id'])
    user = User.objects.get(id=request.POST['user_id'])
    message = request.POST['message']

    #  Check if user has made inquiry already
    if request.user.is_authenticated:
      user_id = request.user.id
      has_contacted = Contact.objects.all().filter(listing=listing_id, user=user)
      if has_contacted:
        messages.error(request, 'You have already made an inquiry for this listing')
        return redirect('/listings/'+listing_no)

    contact = Contact(listing=listing_id, message=message, user=user )

    contact.save()

    # Send email
    # send_mail(
    #  'Property Listing Inquiry',
    #  'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info',
    #  'traversy.brad@gmail.com',
    #  [consultant_email, 'techguyinfo@gmail.com'],
    #  fail_silently=False
    #)

    messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
    return redirect('/listings/'+listing_no)