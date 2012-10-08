from django.conf.urls import patterns, include, url
from myblog.views import PostsListView, PostDetailView, TaggedPostsListView


urlpatterns = patterns('',
    url(r'^$', PostsListView.as_view(), name='post_list'),
    url(r'^tag/(?P<tag>[-\w\d]+)/$',
        TaggedPostsListView.as_view(), 
        name='tagged_post_list'),
    url(r'^(?P<pk>\d+)/(?P<slug>[-\w\d]+)/$',
        PostDetailView.as_view(),
        name='post_detail',
        ),
)
