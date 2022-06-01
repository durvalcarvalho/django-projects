from django.shortcuts import render
from django.contrib.auth.models import User


def main_view(request):
    users = User.objects.all()
    context = { 'users': users }
    return render(request, 'main.html', context)
