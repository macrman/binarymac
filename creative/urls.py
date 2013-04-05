from django.conf.urls import patterns
from .views import IdeaListView

urlpatterns = patterns('',
    (r'(?P<stage>\w+)/$', IdeaListView.as_view()),
)
