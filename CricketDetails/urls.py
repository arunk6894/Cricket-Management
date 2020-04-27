from django.urls import path,include, re_path
from django.conf.urls import url

from CricketDetails.views import Teams,Index,NewTeam,PlayerDetailView,test,NewPlayer,PlayerStatistics

urlpatterns = [
    path('teamdetails/<int:player_details_pk>/<int:pk>/', PlayerStatistics.as_view(), name= 'playerdetails'),
    path('homepage/', Index.as_view(), name = 'index'),
    path('teamdetails/', Teams.as_view(), name = 'teamlist'),
    path('teamdetails/newteam', NewTeam.as_view(), name='newteam'),
    path('teamdetails/<int:pk>/', PlayerDetailView.as_view(), name='teamname'),
    path('teamdetails/newplayers/', NewPlayer.as_view(), name='newplayer'),

    ]