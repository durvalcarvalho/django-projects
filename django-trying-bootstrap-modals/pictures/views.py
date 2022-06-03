from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, View
from django.core import serializers

from pictures.models import Picture


class PicturesListView(ListView):
    template_name = 'pictures/pictures_list.html'
    model = Picture
    context_object_name = 'pictures'


class PictureView(View):
    def get(self, request):
        qs = Picture.objects.all()
        data = serializers.serialize('json', qs)
        return JsonResponse({'data': data})