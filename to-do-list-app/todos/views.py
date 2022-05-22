from django.shortcuts import get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from django.db.models import Q

from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from todos import models


class CustomLoginView(auth_views.LoginView):
    template_name = 'todos/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self) -> str:
        return reverse_lazy('todos:task_list')


class CustomLogoutView(auth_views.LogoutView):
    template_name = 'todos/logged_out.html'


class RegisterView(generic.FormView):
    template_name = 'todos/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('todos:task_list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().get(request, *args, **kwargs)


class TaskList(LoginRequiredMixin, generic.ListView):
    model = models.Task
    template_name = 'todos/task_list.html'
    context_object_name = 'tasks'
    paginate_by = 10

    def get_queryset(self):
        queryset = self.model.objects.filter(user=self.request.user)

        if 'q' in self.request.GET:
            q = self.request.GET['q']

            queryset = queryset.filter(
                Q(title__icontains=q) | Q(description__icontains=q)
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['task_count'] = self.model.objects.filter(user=self.request.user).count()

        if context['task_count']:
            context['task_completed_count'] = self.model.objects.filter(
                user=self.request.user,
                completed=True
            ).count()

            context['perc_completed'] = context['task_completed_count'] / context['task_count']

            context['perc_completed'] = f'{context["perc_completed"] * 100:.2f}%'

        return context


class TaskDetail(LoginRequiredMixin, generic.DetailView):
    model = models.Task
    template_name = 'todos/task_detail.html'
    context_object_name = 'task'

    def get_object(self):
        return get_object_or_404(
            self.model,
            pk=self.kwargs['pk'],
            user=self.request.user
        )

class TaskCreate(LoginRequiredMixin, generic.CreateView):
    model = models.Task
    template_name = 'todos/task_create.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('todos:task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdate(LoginRequiredMixin, generic.UpdateView):
    model = models.Task
    template_name = 'todos/task_update.html'
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('todos:task_list')

    def get_object(self):
        return get_object_or_404(
            self.model,
            pk=self.kwargs['pk'],
            user=self.request.user
        )


class TaskDelete(LoginRequiredMixin, generic.DeleteView):
    model = models.Task
    context_object_name = 'task'
    template_name = 'todos/task_confirm_delete.html'
    success_url = reverse_lazy('todos:task_list')

    def get_object(self):
        return get_object_or_404(
            self.model,
            pk=self.kwargs['pk'],
            user=self.request.user
        )
