from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, View

from docs.models import Doc
# def main_view(request):
#     return render(request, 'docs/main.html')

class MainView(TemplateView):
    template_name = 'docs/main.html'


class FileUploadView(View):
    def post(self, request, *args, **kwargs):
        if file := request.FILES.get('file', None):
            Doc.objects.create(file=file)
            return HttpResponse('file uploaded', status=201)

        return HttpResponse('Fail', status=400)