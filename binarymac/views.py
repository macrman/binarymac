from django.views.generic import TemplateView


class CreativeMethodView(TemplateView):
    template_name = 'creative_method.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


class HomeView(TemplateView):
    template_name = 'home.html'
