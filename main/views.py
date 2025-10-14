from django.shortcuts import render
from django.http import HttpResponse

from main.models import Toilets

def index(request):

    toilets = Toilets.objects.all()

    context = {
        'toilets': toilets
    }

    return render(request, 'main/index.html', context)