from django.views.generic import ListView, DetailView
from django.http import Http404
from binarymac.utils import menulist
from .models import Idea 


class IdeaDetailView(DetailView):

    template_name = 'idea_detail.html'
    model = Idea
    allow_empty = False
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(IdeaDetailView, self).get_context_data(**kwargs)
        kwargs = self.kwargs
        context.update(kwargs)
        active = ["/creations", None]
        context["menu"] = menulist(active)
        return context


class IdeaListView(ListView):

    template_name = 'idea_list.html'
    context_object_name = 'post_list'
    queryset = Idea.objects.all().order_by('-last_updated')

    def get_context_data(self, **kwargs):
        context = super(IdeaListView, self).get_context_data(**kwargs)
        kwargs = self.kwargs
        context.update(kwargs)
        active = ["/creations", None]
        context['menu'] = menulist(active)
        return context
