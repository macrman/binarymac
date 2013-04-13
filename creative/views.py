from django.views.generic import TemplateView
from django.views.generic.base import ContextMixin
from .models import Idea, Stage


class IdeaListMixin(ContextMixin):

    def get_context_data(self, **kwargs):
        stage = self.kwargs.get("stage")
        idea_list = Idea.objects.order_by('-last_updated')
        context = {}
        if stage == "all":
            stage_detail = Stage()
            stage_detail.name = "all"
            stage_detail.info = "blah blah blah... all posts"
        else:
            idea_list = idea_list.filter(stage__name__iexact=stage)
            stage_detail = Stage.objects.get(name__iexact=stage)
        context["stage_detail"] = stage_detail

        if self.kwargs.get("pk"):
            pk = self.kwargs.get("pk")
            current_idea = Idea.objects.get(pk=pk, stage__name__iexact=stage)
            idea_list = idea_list.filter(
                last_updated__lte=current_idea.last_updated
            )
            context["current_idea"] = current_idea

        context["idea_list"] = idea_list
        return super(IdeaListMixin, self).get_context_data(**context)


class IdeaListView(IdeaListMixin, TemplateView):
    template_name = "ideas.html"


class IdeaDetailView(IdeaListMixin, TemplateView):
    template_name = "idea_detail.html"
