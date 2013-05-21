from django.views.generic import ListView, DetailView
from .models import Idea


class IdeaDetailView(DetailView):

    template_name = 'idea_detail.html'
    model = Idea
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super(IdeaDetailView, self).get_context_data(**kwargs)
        kwargs = self.kwargs
        context.update(kwargs)
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
        return context
