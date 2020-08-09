from django.views import generic
from .models import Vacancy

class VacancyList(generic.ListView): 
    queryset = Vacancy.objects.filter(status=1).order_by('-created_on')
    template_name = 'jobportal/vacancy.html'

class VacancyDetail(generic.DetailView):
    model = Vacancy
    template_name = 'jobportal/vacancy_detail.html'