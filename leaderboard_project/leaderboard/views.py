# views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import Player
from django.views.decorators.csrf import csrf_exempt
import json

#def index(request):
#    return render(request, 'index.html')

def index(request):
    players = Player.objects.order_by('-score')[:100]  # Получение топ-10 игроков (сортировка по счету)
    context = {'players': players}
    return render(request, 'index.html', context)

@csrf_exempt
def add_score_to_leaderboard(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        score = data.get('score')

        player = Player(name=name, score=score)
        player.save()

        return JsonResponse({'message': 'Данные успешно добавлены в таблицу лидеров'})
    else:
        return JsonResponse({'message': 'Метод запроса не разрешен'}, status=405)

# Create your views here.
