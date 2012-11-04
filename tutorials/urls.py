from django.conf.urls import patterns, include, url
from tutorials.views import TutorialListView, TutorialDetailView

urlpatterns = patterns('',
    url(
        r'^$',
        TutorialListView.as_view(), 
        name = "tutorial_list",
    ),
)

    #    url(
    #    r'^(\w+)/$',
    #   TutorialDetailView.as_view(),
    #   "tutorial_detail",
  # ),
