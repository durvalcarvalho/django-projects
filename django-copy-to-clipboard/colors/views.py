from django.shortcuts import render
from django.views.generic import ListView

from colors.models import Color


class ColorListView(ListView):
    model = Color
    template_name = 'colors/list_colors.html'
    context_object_name = 'colors'