from django.views.generic import TemplateView
from .utils import menulist


class CreativeMethodView(TemplateView):
    template_name = 'creative_method.html'

    def get_context_data(self, **kwargs):
        context = super(CreativeMethodView, self).get_context_data(**kwargs)
        active = ['/creative_method', None]
        context['menu'] = menulist(active)
        return context


class ContactView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        active = ['/contact', None]
        context['menu'] = menulist(active)
        return context


class HomeView(TemplateView):
    template_name = 'home.html'
