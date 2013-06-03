from django.views.generic import ListView, DetailView, TemplateView
from binarymac.utils import menulist
from .models import Idea


class ImplementationListView(TemplateView):

    template_name = 'implementation_list.html'

    def get_context_data(self, **kwargs):
        context = super(ImplementationListView, self).get_context_data(**kwargs)
        active = ["/creations", "/creations/implementation"]
        context["menu"] = menulist(active)
        return context


class IdeaDetailView(DetailView):

    template_name = 'idea_detail.html'
    model = Idea
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super(IdeaDetailView, self).get_context_data(**kwargs)
        kwargs = self.kwargs
        context.update(kwargs)
        active = ["/creations", None]
        context["menu"] = menulist(active)
        return context


class IdeaListView(ListView):

    template_name = 'idea_list.html'
    allow_empty = False

    def dehumanize(self):
        for choice in Idea.STAGE_CHOICES:
            if self.kwargs.get('stage') in choice:
                dehumanized = choice[0]
                return dehumanized

    def get_queryset(self):
        if self.kwargs.get('stage') == 'everything':
            queryset = Idea.objects.all()
        else:
            queryset = Idea.objects.filter(stage=self.dehumanize())
        return queryset

    def get_context_data(self, **kwargs):
        context = super(IdeaListView, self).get_context_data(**kwargs)
        kwargs = self.kwargs
        context.update(kwargs)
        active = ["/creations", "/creations/" + self.kwargs.get('stage')]
        context['menu'] = menulist(active)
        return context
