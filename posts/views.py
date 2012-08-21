from django.views.generic import ListView
from posts.models import Post


class PostsListView(ListView):
    model = Post
    template_name = 'posts_page.html'
