from django.urls import include, path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/create-toilet/', views.toilet_api),

    path('api/getcomments_api/', views.getComments_api),
    path('api/addComment_api/', views.addComment_api),

    path('api/addReview_api/', views.addReviews_api),    
    path('api/getReview_api/', views.getReview_api),
]

