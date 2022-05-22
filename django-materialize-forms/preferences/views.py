from django.views.generic import FormView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from preferences.forms import PreferenceModelForm


class MyPreferenceFormView(LoginRequiredMixin, FormView):
    form_class = PreferenceModelForm
    template_name = 'preferences/main.html'

    def get_success_url(self) -> str:
        return self.request.path

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Your preferences have been saved.')
        return super().form_valid(form)

    def form_invalid(self, form):
        form.add_error(
            None,
            'Please correct the errors below and try again.',
        )
        return super().form_invalid(form)

