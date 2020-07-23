from django.urls import path, re_path
from .views import room


app_name = 'chatchannels'

urlpatterns = [
    re_path(r'^(?P<room_name>[^/]+)/$', room, name='room'),
]
