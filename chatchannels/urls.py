from django.urls import path, re_path
from . import views


#app_name = 'chatchannels'

urlpatterns = [
   re_path(r'^(?P<room_name>[^/]+)/$', views.room, name='chat'),
]
