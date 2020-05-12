from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_rooms, name="all_rooms"),
    url(r'token$', views.token, name="token"),
    url('rooms/(?P<slug>[-\w]+)/$', views.room_detail, name="room_detail")
]