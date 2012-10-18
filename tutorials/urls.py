from django.conf.urls import patterns, include, url
from tutorials.views import TutorialListView

urlpatterns = patterns('',
    url(
        regex=r'^$',
        view=TutorialListView.as_view(), 
        name="tutorial_list"
    ),
    url(
        regex=r'^+\w$',
        view=TutorialDetailview.as_view(),
        name="tutorial_detail"
    ),
)
