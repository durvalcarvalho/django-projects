from django.contrib import admin

from posts.models import Post, Comment, Like


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Meta:
        model = Post

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    class Meta:
        model = Comment


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    class Meta:
        model = Like
