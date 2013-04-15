from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, patterns, include
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    "",
    url(r'^admin/', include(admin.site.urls)),
    url(r'^creations/', include('creative.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
