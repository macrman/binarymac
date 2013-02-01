from creative.models import Idea
from django.views.generic import ListView


class IdeaListView(ListView):
    model = Idea()
    template_name = 'home.html'
