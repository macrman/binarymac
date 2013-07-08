from django.conf.urls import url, patterns
from .views import (
    IdeaDetailView, IdeaListView, ImplementationListView,
    ImplementationDetailView)

urlpatterns = patterns(
    '',
    url(
        r'(?P<pk>\d+)/(?P<slug>[-\w\d]+)/$',
        IdeaDetailView.as_view(),
        name='idea_detail',
    ),
    url(
        r'^$',
        IdeaListView.as_view(),
        name="idea_list",
    )
)
