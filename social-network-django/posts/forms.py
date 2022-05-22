from django import forms


from posts.models import Post, Comment


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))

    class Meta:
        model = Post
        fields = [
            'content',
            'image',
        ]


class CommentForm(forms.ModelForm):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={
                'rows': 2,
                'placeholder': 'Add a comment',
            },
        ),
    )

    class Meta:
        model = Comment
        fields = [
            'body',
        ]
