from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
import chat.views as chat


urlpatterns = [
    path('', include('pages.urls')),
    path('listings/', include('listings.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('chatapp/', include('chatapp.urls')),
    path('rooms/', include('chat.urls')),
    url('rooms/(?P<slug>[-\w]+)/$', chat.room_detail, name="room_detail")
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)