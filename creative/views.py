from django.views.generic import TemplateView
from .models import Idea


# dpaste.org/Ik9wA/
class IdeaListView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        experimentation_list = Idea.objects.filter(
            stage__name="Experimentation"
        )
        incubation_list = Idea.objects.filter(
            stage__name="Incubation"
        )
        implementation_list = Idea.objects.filter(
            stage__name="Implementation"
        )

        context = {
            'experimentation_list': experimentation_list,
            'incubation_list': incubation_list,
            'implementation_list': implementation_list,
        }
        return super(IdeaListView, self).get_context_data(**context)
