from django.conf.urls import patterns, include, url
from binarymac.views import home
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', home.as_view(), name='home'),
    # url(r'^binarymac/', include('binarymac.foo.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
