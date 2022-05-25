from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class MainTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'main.html'
