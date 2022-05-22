from django.shortcuts import render
from django.http import JsonResponse

from images.models import Image
from images.forms import ImageForm


def main_view(request):
    form = ImageForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return JsonResponse({'message': 'Image uploaded successfully'})

    context = { 'form': form }
    return render(request, 'images/main.html', context)
