from django.urls import include, path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/create-toilet/', views.toilet_api, name='toilet_api'),
    path('api/comments_api/', views.comments_api, name='toilet_api'),
]
