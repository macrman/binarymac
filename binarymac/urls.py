from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, patterns, include
from django.contrib import admin
from .views import CreativeMethodView, ContactView, HomeView

admin.autodiscover()

urlpatterns = patterns(
    "",
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^admin/', include(admin.site.urls)),
    url(
        r'^creative_method/',
        CreativeMethodView.as_view(),
        name="creative_method",
    ),
    url(r'contact/', ContactView.as_view(), name="contact",),
    url(r'^creations/', include('creative.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
