from django.views.generic import ListView, DetailView, TemplateView
from myblog.models import Post


class PostListView(ListView):
    model = Post
    queryset = Post.objects.order_by("-pub_date")
    paginate_by = '2' 
    context_object_name = 'post_list'
    template_name = 'blog.html'


class PostDetailView(DetailView):
    model = Post
    template_name = "blog.html"
    context_object_name = "post"


class TaggedPostsListView(TemplateView):
    template_name = 'blog.html'
