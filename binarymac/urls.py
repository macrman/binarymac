from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include
from django.contrib import admin
import creative

admin.autodiscover()

urlpatterns = patterns(
    "",
    (r'^admin/', include(admin.site.urls)),
    (r'^creations/', include('creative.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
