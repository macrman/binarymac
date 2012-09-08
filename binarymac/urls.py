from django.conf.urls import patterns, include, url
from binarymac.views import HomePageView
from django.contrib import admin
from simplepages.views import PageDetailView
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', HomePageView.as_view(), name="home_view"),
    url(r'^learn/$', TemplateView.as_view(template_name="home.html"), name="learn_view"),
    url(r'^look/$', TemplateView.as_view(template_name="home.html"), name="look_view"),
    url(r'^read/$', TemplateView.as_view(template_name="home.html"), name="read_view"),
    url(r'^blog/', include('myblog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<slug>[-\w\d]+)/$', PageDetailView.as_view(), name="page_detail")
)
