from django import forms


from images.models import Image


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('file',)