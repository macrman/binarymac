from django.views.generic import DetailView
from simplepages.models import Page


class PageDetailView(DetailView):
    template_name = "page_detail.html"
    model = Page
    template_object_name = "page"
