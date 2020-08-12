from django.views import generic
from django.shortcuts import get_object_or_404, render
from .models import Vacancy
from .choices import minexperience_choices, specialization_choices

class VacancyList(generic.ListView): 
    queryset = Vacancy.objects.filter(status=1).order_by('-created_on')
    template_name = 'jobportal/vacancy.html'

class VacancyDetail(generic.DetailView):
    model = Vacancy
    template_name = 'jobportal/vacancy_detail.html'

def searchjob(request):
  queryset_list = Vacancy.objects.order_by('-created_on')

  # Keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      queryset_list = queryset_list.filter(title__icontains=keywords)

  # Area
  if 'area' in request.GET:
    area = request.GET['area']
    if area: 
      queryset_list = queryset_list.filter(area__iexact=area)

  # Experience
  if 'minexperience' in request.GET:
    minexperience = request.GET['minexperience']
    if minexperience:
      queryset_list = queryset_list.filter(experience_required__gte=minexperience)

  # Specialization
  if 'specialization' in request.GET:
    specialization = request.GET['specialization']
    if specialization:
      queryset_list = queryset_list.filter(specialization__iexact=specialization)


  context = {
      'minexperience_choices': minexperience_choices,
      'specialization_choices': specialization_choices,
      'vacancies': queryset_list,
      'values': request.GET
  }

  return render(request, 'jobportal/search.html', context)