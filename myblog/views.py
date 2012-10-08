from django.views.generic import ListView, DetailView, TemplateView
from myblog.models import Post


class PostsListView(ListView):
    model = Post
    template_name = 'post_list.html'


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    template_object_name = "post"

class TaggedPostsListView(TemplateView):
    template_name = 'post_list.html'
