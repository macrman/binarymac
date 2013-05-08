from django.conf.urls import url, patterns
from .views import IdeaListView, IdeaListAndDetailView

urlpatterns = patterns(
    '',
    url(
        r'(?P<stage>\w+)/(?P<pk>\d+)/$',
        IdeaListAndDetailView.as_view(),
        name="idea_detail",
    ),
    url(
        r'(?P<stage>\w+)/$',
        IdeaListView.as_view(),
        name="idea_list",
    ),
)
