#urls.py
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import add_score_to_leaderboard

urlpatterns = [
    path('', views.index, name='index'),
    path('UnityLoader/', views.add_score_to_leaderboard, name='UnityLoader'),
]
urlpatterns += staticfiles_urlpatterns()