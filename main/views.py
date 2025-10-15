from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

from main.models import Toilets

def index(request):

    toilets = Toilets.objects.all()

    context = {
        'toilets': toilets
    }

    return render(request, 'main/index.html', context)


@csrf_exempt
def toilet_api(request):
    
    if request.method == 'POST':
        # Создать новый туалет
        data = json.loads(request.body)
        toilet = Toilets.objects.create(
            name=data['name'],
            coords1=data['coords1'],
            coords2=data['coords2']
        )
        return JsonResponse({'id': toilet.id, 'success': True})
