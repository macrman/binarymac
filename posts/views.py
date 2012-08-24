from django.views.generic import ListView, DetailView
from posts.models import Post


class PostsListView(ListView):
    model = Post
    template_name = 'posts_page.html'
    template_object_name = 'poll'


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
