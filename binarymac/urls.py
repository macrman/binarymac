from django.conf.urls import patterns, include, url
from binarymac.views import HomePageView
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', HomePageView.as_view(), name="home_view"),
    url(r'^learn/', include('tutorials.urls')),
    url(r'^look/$', TemplateView.as_view(template_name="home.html"), name="portfolio_view"),
    url(r'^blog/', include('myblog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
