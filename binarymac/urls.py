from django.conf.urls import patterns, include, url
from binarymac.views import HomePageView
from django.contrib import admin
from simplepages.views import PageDetailView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', HomePageView.as_view(), name="home_page_view"),
    url(r'^blog/', include('myblog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<slug>[-\w\d]+)/$', PageDetailView.as_view(), name="page_detail")
)
