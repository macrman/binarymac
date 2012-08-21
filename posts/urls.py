from django.conf.urls import patterns, include, url
from posts.views import PostsListView

urlpatterns = patterns('',
    url(r'^$', PostsListView.as_view(), name='Posts Page'),
)
