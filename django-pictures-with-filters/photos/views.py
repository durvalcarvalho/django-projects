from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import CreateView

from photos.models import Upload


class UploadCreateView(CreateView):
    model = Upload
    fields = ['image', 'action']
    template_name = 'photos/upload_form.html'
