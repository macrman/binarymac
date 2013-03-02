from django.views.generic import ListView
from .models import Idea


class IdeaListView(ListView):
    model = Idea()
    template_name = "home.html"
