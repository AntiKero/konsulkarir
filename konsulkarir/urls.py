from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url


urlpatterns = [
    path('', include('pages.urls')),
    path('listings/', include('listings.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('contacts/', include('contacts.urls')),
    path('chat/', include('chatchannels.urls', namespace='chat')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)