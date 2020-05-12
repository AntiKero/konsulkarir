from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'consultant', 'price', 'list_date', 'is_published')
  list_display_links = ('id', )
  list_filter = ('consultant',)
  list_editable = ('is_published',)
  search_fields = ('id', 'consultant', 'price', 'list_date', )
  list_per_page = 25

  def first_name(self, obj):
        return obj.user.first_name 

  def last_name(self, obj):
        return obj.user.last_name

  def email(self, obj):
        return obj.user.email

admin.site.register(Listing, ListingAdmin)