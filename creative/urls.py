from django.conf.urls import patterns
from .views import IdeaListView, IdeaDetailView

urlpatterns = patterns(
    '',
    (r'(?P<stage>\w+)/(?P<pk>\d+)/$', IdeaDetailView.as_view()),
    (r'(?P<stage>\w+)/$', IdeaListView.as_view()),
)
