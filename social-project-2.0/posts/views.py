from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse

from posts import models
from profiles.models import Profile


class HomeView(generic.TemplateView):
    template_name = 'posts/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.last()
        return context


class PostsListView(generic.ListView):
    model = models.Post
    template_name = 'posts/posts_list.html'
    context_object_name = 'posts'


class JsonPostListView(generic.View):
    def get(self, request):
        posts = models.Post.objects.all()
        data = [ post.to_json() for post in posts ]
        return JsonResponse({'posts': data})