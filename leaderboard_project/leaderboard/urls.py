from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import add_score_to_leaderboard

urlpatterns = [
    path('', views.index, name='index'),
    path('add_score/', views.add_score_to_leaderboard, name='add_score'),
]
urlpatterns += staticfiles_urlpatterns()