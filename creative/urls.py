from django.conf.urls import url, patterns
from .views import IdeaDetailView, IdeaListView

urlpatterns = patterns(
    '',
    url(
        r'(?P<pk>\d+)$',
        IdeaDetailView.as_view(),
        name='idea_detail',
    ),
    url(
        r'^$',
        IdeaListView.as_view(),
        name="idea_list",
    )
)
