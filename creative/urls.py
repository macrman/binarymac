from django.conf.urls import url, patterns
from .views import (
    IdeaDetailView, IdeaListView, ImplementationListView,
    ImplementationDetailView)

urlpatterns = patterns(
    '',
    url(
        r'^(?P<stage>implementation)/$',
        ImplementationListView.as_view(),
        name='implementation_list',
    ),
    url(
        r'^(?P<stage>implementation)/(?P<pk>\d+)/(?P<slug>\w+)/$',
        ImplementationDetailView.as_view(),
        name='implementation_detail',
    ),
    url(
        r'(?P<stage>\w+)/(?P<pk>\d+)/(?P<slug>\w+)/$',
        IdeaDetailView.as_view(),
        name='idea_detail',
    ),
    url(
        r'(?P<stage>\w+)/$',
        IdeaListView.as_view(),
        name='idea_list',
    ),
    url(
        r'^$',
        IdeaListView.as_view(),
        name="idea_list",
    )
)
