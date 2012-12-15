from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from myblog.models import Post, Tag


class PostListView(ListView):
    model = Post
    queryset = Post.objects.order_by("-pub_date")
    paginate_by = '2'
    context_object_name = 'post_list'
    template_name = 'blog/blog.html'


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/blog.html"
    context_object_name = "post"


class TaggedPostsListView(ListView):
    template_name = 'blog/blog.html'
    context_object_name = 'post_list'
    paginate_by = '2'

    def get_queryset(self):
        self.tag = get_object_or_404(Tag, name__iexact=self.args[0])
        return Post.objects.filter(tag=self.tag)
