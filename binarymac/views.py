from django.views.generic import TemplateView, RedirectView
from django.core.urlresolvers import reverse_lazy


class CreativeMethodView(TemplateView):
    template_name = 'creative_method.html'
