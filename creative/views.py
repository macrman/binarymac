from django.views.generic import ListView, TemplateView
from .models import Idea


class IdeaListView(TemplateView):
    template_name = "creations.html"
    model = Idea

    def get_context_data(self, **kwargs):
        mykwargs = self.kwargs['stage']
        if mykwargs == "all":
            context = {"idea_list": Idea.objects.all()}
        else:
            context = {
                "idea_list": Idea.objects.filter(stage__name__iexact=mykwargs)
            }
        return super(IdeaListView, self).get_context_data(**context)


class ExperimentationListView(ListView):
    pass
