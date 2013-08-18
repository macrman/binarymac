from django.views.generic import ListView, DetailView
from django.http import Http404
from .models import Idea 


class IdeaDetailView(DetailView):

    template_name = 'idea_detail.html'
    model = Idea
    allow_empty = False
    context_object_name = 'post'


class IdeaListView(ListView):

    template_name = 'idea_list.html'
    context_object_name = 'post_list'
    queryset = Idea.objects.all().order_by('-last_updated')
