from tutorials.models import Tutorial
from django.views.generic import DetailView, ListView, TemplateView


class TutorialDetailView(TemplateView):
    template_name="home.html"
    #    template_name = "tutorial_detail.html"
#    model = Tutorial
# Detail View

#     get the path to the object
#        open the object 
    #        convert rst > html
#                OR
#            leave as rst
#     return the objects to context

#        convert to html if needed


class TutorialListView(TemplateView):
    template_name="home.html"
