from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

from main.models import Toilets, Comments, Reviews

def index(request):

    toilets = Toilets.objects.all()


    context = {
        'toilets': toilets
    }

    return render(request, 'main/index.html', context)


@csrf_exempt
def toilet_api(request):
    
    if request.method == 'POST':
        data = json.loads(request.body)
        toilet = Toilets.objects.create(
            name=data['name'],
            coords1=data['coords1'],
            coords2=data['coords2']
        )
        return JsonResponse({'id': toilet.id, 'success': True})




def getComments_api(request):
    x = request.GET.get('currentToilet')
    currentToilet = Toilets.objects.filter(name=x)[0]
    comments = Comments.objects.filter(toilet=currentToilet)
    commentsList = []
    for comment in comments:
        oneComm = {
            'text': comment.text,
        }
        commentsList.append(oneComm)

    return JsonResponse(commentsList, safe=False)

@csrf_exempt
def addComment_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        currentToilet= Toilets.objects.filter(name=data['toiletName'])[0]
        Comment = Comments.objects.create(
            text=data['text'],
            toilet=currentToilet
        )
        return JsonResponse({'id': Comment.id, 'success': True})




def getReview_api(request):
    x = request.GET.get('currentToilet')
    currentToilet = Toilets.objects.filter(name=x)[0]
    reviews = Reviews.objects.filter(toilet=currentToilet)
    generalReview = 0
    size = 0
    for review in reviews:
        generalReview += review.estimation
        size += 1
    if (size != 0):
        generalReview /= size
        generalReview = float("{0:.1f}".format(generalReview))
    
    return JsonResponse(generalReview, safe=False)

@csrf_exempt
def addReviews_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        currentToilet= Toilets.objects.filter(name=data['toiletName'])[0]
        review = Reviews.objects.create(
            estimation=data['myReview'],
            toilet=currentToilet
        )
        return JsonResponse({'id': review.id, 'success': True})