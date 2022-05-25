from django.views.generic import TemplateView


class MainTemplateView(TemplateView):
    template_name = 'main.html'
