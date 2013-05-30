from django.views.generic import ListView, DetailView, TemplateView
from .models import Idea


def menulist():
    nested = [
        {'name': "Incubation", 'url': '/creations/incubation', 'active': False, },
        {'name': "Analyzation", 'url': '/creations/analyzation', 'active': False, },
        {'name': "Experimentation", 'url': '/creations/experimentation', 'active': False, },
        {'name': "Implementation", 'url': '/creations/implementation', 'active': False, },
        {'name': "Documentation", 'url': '/creations/documentation', 'active': False, },
    ]

    menu = [
        {
            'name': "Home",
            'url': '/',
            'active': False,
            'nested': None,
        },
        {
            'name': "Creative Method",
            'url': '/creative_method',
            'active': False,
            'nested': None,
        },
        {
            'name': "Ideas & Creations",
            'url': '/creations',
            'active': False,
            'nested': nested,
        },
        {
            'name': "Contact",
            'url': '/contact',
            'active': False,
            'nested': None,
        },
    ]
    return menu


class ImplementationListView(TemplateView):

    template_name = 'implementation_list.html'

    def get_context_data(self, **kwargs):
        context = super(ImplementationListView, self).get_context_data(**kwargs)
        context["menu"] = menulist()
        return context


class IdeaDetailView(DetailView):

    template_name = 'idea_detail.html'
    model = Idea
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super(IdeaDetailView, self).get_context_data(**kwargs)
        kwargs = self.kwargs
        context.update(kwargs)
        context["menu"] = menulist()
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
        context['menu'] = menulist()
        return context
