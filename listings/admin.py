from django.contrib import admin

from .models import Listing, Tag

class ListingAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'consultant', 'price', 'list_date', 'is_published')
  list_display_links = ('id', )
  list_filter = ('consultant',)
  list_editable = ('is_published',)
  search_fields = ('id', 'consultant', 'price', 'list_date', )
  list_per_page = 25

  def get_queryset(self, request):
      qs = super(ListingAdmin, self).get_queryset(request)
      if request.user.is_superuser:
            return qs
      return qs.filter(consultant__user_id=request.user)

  def first_name(self, obj):
        return obj.user.first_name 

  def last_name(self, obj):
        return obj.user.last_name

  def email(self, obj):
        return obj.user.email

class TagAdmin(admin.ModelAdmin):
  list_display = ('id', 'tag_name',)
  list_display_links = ('id', 'tag_name',)
  search_fields = ('tag_name',)
  list_per_page = 25       

admin.site.register(Listing, ListingAdmin)
admin.site.register(Tag, TagAdmin)