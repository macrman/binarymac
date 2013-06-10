from django.views.generic import ListView, DetailView
from django.http import Http404
from binarymac.utils import menulist
from .models import Idea, Project


class ImplementationDetailView(ListView):

    template_name = 'idea_list.html'
    context_object_name = 'post_list'

    def get_queryset(self, **kwargs):
        project = Project.objects.get(pk=self.kwargs.get('pk'))
        queryset = Idea.objects.filter(project=project).order_by('-last_updated')
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ImplementationDetailView, self).get_context_data(**kwargs)
        active = ["/creations", "/creations/implementation"]
        context['menu'] = menulist(active)
        return context


class ImplementationListView(ListView):

    template_name = 'implementation_list.html'
    queryset = Project.objects.all()
    context_object_name = 'post_list'

    def get_context_data(self, **kwargs):
        context = super(ImplementationListView, self).get_context_data(**kwargs)
        active = ["/creations", "/creations/implementation"]
        context["menu"] = menulist(active)
        return context


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

    def dehumanize(self):
        for choice in Idea.STAGE_CHOICES:
            if self.kwargs.get('stage') in choice:
                dehumanized = choice[0]
                return dehumanized

    def get_queryset(self):
        if self.kwargs.get('stage'):
            queryset = Idea.objects.filter(stage=self.dehumanize()).order_by('-last_updated')
        else:
            queryset = Idea.objects.all().order_by('-last_updated')
        return queryset

    def get_context_data(self, **kwargs):
        context = super(IdeaListView, self).get_context_data(**kwargs)
        kwargs = self.kwargs
        context.update(kwargs)
        if self.kwargs.get('stage') is None:
            active = ["/creations", None]
        else:
            active = ["/creations", "/creations/" + self.kwargs.get('stage')]
        context['menu'] = menulist(active)
        return context
