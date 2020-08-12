from . import views
from django.urls import path

urlpatterns = [
    path('', views.VacancyList.as_view(), name='vacancy'),
    path('<slug:slug>/', views.VacancyDetail.as_view(), name='vacancy_detail'),
    path('search', views.searchjob, name='searchjob'),
]