from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from creative.views import IdeaListView

admin.autodiscover()

urlpatterns = patterns("",
    (r'^admin/', include(admin.site.urls)),
    (r'^$', IdeaListView.as_view()),
)
