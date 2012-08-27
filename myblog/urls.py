from django.conf.urls import patterns, include, url
from myblog.views import PostsListView, PostDetailView


urlpatterns = patterns('',
    url(r'^$', PostsListView.as_view(), name='posts_list'),
    url(r'^(?P<pk>\d+)$', PostDetailView.as_view(), name='post_detail'),
)
