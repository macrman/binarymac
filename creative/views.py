from django.views.generic import TemplateView
from .models import Idea


class DetailAndListMixin(object):

    def get_idea_list(self, stage):
        '''
        Gets all ideas belonging to a stage, newest first. If no arguments are
        passed, it will get all ideas.
        '''
        all_ideas = Idea.objects.order_by('-last_updated')
        if stage == "everything":
            idea_list = all_ideas
        else:
            idea_list = all_ideas.filter(stage__name__iexact=stage)
        return idea_list

    def get_idea_list_and_obj_from_pk(self, queryset, pk):
        '''
        Takes a queryset and only returns objects equal to or later than the
        object specified by the pk
        '''
        current_idea = queryset.get(pk=pk)
        filtered_queryset = queryset.filter(
            last_updated__lte=current_idea.last_updated
        )
        context = {
            "current_idea": current_idea,
            "idea_list": filtered_queryset,
        }
        return context


class IdeaListView(DetailAndListMixin, TemplateView):
    '''
    Gets all ideas, returns them
    '''
    template_name = "ideas.html"

    def get_context_data(self, **kwargs):
        context = {}
        context['idea_list'] = self.get_idea_list(self.kwargs.get('stage'))
        context.update(kwargs)
        return super(IdeaListView, self).get_context_data(**context)


class IdeaListAndDetailView(DetailAndListMixin, TemplateView):
    '''
    Gets all ideas equal to or updated later than the object from the specified
    pk. Also returns a detailed view of that pk.

    Ex: a request to /all/2/hello-world will return an idea_list of all ideas
    updated later than hello-world. hello-world will be in the idea_list as
    well. A hello-world detail view object will also be returned.
    '''
    template_name = "idea_detail.html"

    def get_context_data(self, **kwargs):
        context = {}
        all_ideas = self.get_idea_list(self.kwargs.get('stage'))
        objs = self.get_idea_list_and_obj_from_pk(all_ideas, self.kwargs['pk'])
        context.update(objs)
        context.update(self.kwargs)
        return super(IdeaListAndDetailView, self).get_context_data(**context)
