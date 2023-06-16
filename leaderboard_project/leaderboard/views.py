from django.shortcuts import render
from .models import Player

#def index(request):
#    return render(request, 'index.html')

def index(request):
    players = Player.objects.order_by('-score')[:10]  # Получение топ-10 игроков (сортировка по счету)
    context = {'players': players}
    return render(request, 'index.html', context)

# Create your views here.
