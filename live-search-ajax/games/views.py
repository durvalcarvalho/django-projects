from copyreg import constructor
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, View


from games.models import Game


class GameListView(ListView):
    model = Game
    context_object_name = 'games'
    template_name = 'games/game_list.html'


class GameDetailView(DetailView):
    model = Game
    context_object_name = 'game'
    template_name = 'games/game_detail.html'



class SearchView(View):
    def post(self, request):
        search = request.POST.get('search')
        games = Game.objects.filter(name__icontains=search)
        return JsonResponse({'games': [game.to_json() for game in games]})