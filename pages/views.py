from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import topic_choices, experience_choices, type_choices

from listings.models import Listing
from consultants.models import Consultant

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'topic_choices': topic_choices,
        'experience_choices': experience_choices,
        'type_choices': type_choices
    }

    return render(request, 'pages/index.html', context)


def about(request):
    # Get all consultants
    consultants = Consultant.objects.order_by('-hire_date')

    # Get MVP
    mvp_consultants = Consultant.objects.all().filter(is_mvp=True)

    context = {
        'consultants': consultants,
        'mvp_consultants': mvp_consultants
    }

    return render(request, 'pages/about.html', context)