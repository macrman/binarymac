from django.conf.urls import url, patterns
from .views import (IdeaDetailView, IdeaListView, ImplementationListView,)

urlpatterns = patterns(
    '',
    url(
        r'(?P<stage>implementation)/$',
        ImplementationListView.as_view(),
        name='implementation_list',
    ),
    url(
        r'(?P<stage>\w+)/(?P<pk>\d+)/$',
        IdeaDetailView.as_view(),
        name='idea_detail',
    ),
    url(
        r'(?P<stage>\w+)/$',
        IdeaListView.as_view(),
        name='idea_list',
    ),
)
