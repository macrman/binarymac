from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.contrib import admin
from creative.views import IdeaListView

admin.autodiscover()

urlpatterns = patterns(
    "",
    (r'^admin/', include(admin.site.urls)),
    (r'^$', IdeaListView.as_view()),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
