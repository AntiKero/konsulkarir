from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
  list_display = ('id', 'username', 'first_name', 'last_name', 'email', 'contact_date')
  list_display_links = ('id', 'username')
  list_per_page = 25

  def username(self, obj):
        return obj.user.username
  
  def first_name(self, obj):
        return obj.user.first_name 

  def last_name(self, obj):
        return obj.user.last_name

  def email(self, obj):
        return obj.user.email

admin.site.register(Contact, ContactAdmin)