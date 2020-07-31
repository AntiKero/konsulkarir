from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import topic_choices, experience_choices, type_choices

from .models import Listing
from consultants.models import Consultant, Job
def index(request):
  listings = Listing.objects.order_by('-list_date').filter(is_published=True)

  paginator = Paginator(listings, 6)
  page = request.GET.get('page')
  paged_listings = paginator.get_page(page)

  context = {
    'listings': paged_listings
  }

  return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
  listing = get_object_or_404(Listing, pk=listing_id)

  context = {
    'listing': listing
  }

  return render(request, 'listings/listing.html', context)

def search(request):
  queryset_list = Listing.objects.order_by('-list_date')

  # Keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      queryset_list = queryset_list.filter(title__icontains=keywords)

  # Tag
  if 'tag' in request.GET:
    tag = request.GET['tag']
    if tag: 
      queryset_list = queryset_list.filter(consultant__tag__tag_name__iexact=tag)


  # Experience
  if 'experience' in request.GET:
    experience = request.GET['experience']
    if experience:
      queryset_list = queryset_list.filter(consultant__job_experience__gte=experience)

  # job_type
  if 'job_type' in request.GET:
    job_type = request.GET['job_type']
    if job_type == "HR":
      queryset_list = queryset_list.filter(consultant__job__job_type__iexact=job_type)
    else:
      queryset_list = queryset_list.exclude(consultant__job__job_type="HR")


  context = {
      'topic_choices': topic_choices,
      'experience_choices': experience_choices,
      'type_choices': type_choices,
      'listings': queryset_list,
      'values': request.GET
  }

  return render(request, 'listings/search.html', context)