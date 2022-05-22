from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


from posts.models import Like, Post
from posts import forms

@login_required
def post_comment_create_and_list_view(request):
    posts = Post.objects.all()
    profile = request.user.profile

    post_form = forms.PostForm(request.POST or None, request.FILES or None)
    comment_form = forms.CommentForm(request.POST or None)

    if post_form.is_valid():
        post_instance = post_form.save(commit=False)
        post_instance.author = profile
        post_instance.save()

    if comment_form.is_valid():
        comment_instance = comment_form.save(commit=False)
        comment_instance.user = profile
        post = get_object_or_404(Post, id=request.POST.get('post_id'))
        comment_instance.post = post
        comment_instance.save()

    context = {
        'posts': posts,
        'profile': profile,
        'post_form': post_form,
        'comment_form': comment_form,
    }

    return render(request, 'posts/main.html', context)

@login_required
def like_or_unlike_post(request):
    if request.method != 'POST':
        return redirect('posts:main-post-view')

    profile = request.user.profile

    post_id = request.POST.get('post_id')
    post = Post.objects.get(id=post_id)

    if profile in post.liked.all():
        post.liked.remove(profile)

    else:
        post.liked.add(profile)

    like, created = Like.objects.get_or_create(user=profile, post=post)

    if not created and like.value == Like.LikeValues.LIKE:
        like.value = Like.LikeValues.DISLIKE
    else:
        like.value = Like.LikeValues.LIKE

    like.save()
    post.save()

    return redirect('posts:main-post-view')



class PostDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    template_name = 'posts/confirm_delete.html'
    success_url = reverse_lazy('posts:main-post-view')

    def get_object(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])

        if post.author.user != self.request.user:
            messages.warning(self.request, 'You are not allowed to delete this post.')
            return None

        return post

class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    form_class = forms.PostForm
    model = Post
    template_name = 'posts/post_update.html'
    success_url = reverse_lazy('posts:main-post-view')

    def form_valid(self, form):
        profile = self.request.user.profile

        if form.instance.author != profile:
            messages.warning(self.request, 'You are not allowed to edit this post.')
            form.add_error(None, 'You are not allowed to edit this post.')
            return self.form_invalid(form)

        return super().form_valid(form)


    # def get_object(self, *args, **kwargs):
    #     post = get_object_or_404(Post, pk=self.kwargs['pk'])

    #     if post.author.user != self.request.user:
    #         raise PermissionDenied(
    #             'You are not allowed to update this post.'
    #         )

    #     return post