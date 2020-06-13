from django.contrib import admin

from .models import Consultant, Job


class ConsultantAdmin(admin.ModelAdmin):
  list_display = ('id', 'first_name', 'last_name', 'email', 'join_date')
  list_display_links = ('id', 'first_name', 'last_name', )
  search_fields = ('name',)
  list_per_page = 25

  def id(self, obj):
        return obj.user.username
  
  def first_name(self, obj):
        return obj.user.first_name 

  def last_name(self, obj):
        return obj.user.last_name

  def email(self, obj):
        return obj.user.email


class JobAdmin(admin.ModelAdmin):
  list_display = ('id', 'job_name', 'job_type',)
  list_display_links = ('id', 'job_name',)
  search_fields = ('job_name',)
  list_per_page = 25



admin.site.register(Consultant, ConsultantAdmin,)
admin.site.register(Job, JobAdmin,)
