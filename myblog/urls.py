from django.conf.urls import patterns, include, url
from myblog.views import PostsListView, PostDetailView


urlpatterns = patterns('',
    url(r'^index/$', PostsListView.as_view(), name='post_list'),
    url(r'^(?P<pk>\d+)/(?P<slug>[-\w\d]+)/$',
        PostDetailView.as_view(),
        name='post_detail',
        ),
)
