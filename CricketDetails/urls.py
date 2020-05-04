from django.urls import path,include, re_path
from django.conf.urls import url

from CricketDetails.views import (Teams,Index,NewTeam,PlayerDetailView,test,NewPlayer,PlayerStatistics,
Fixtures,Fixtures_Form,BatStatistics,BowlStatistics,ScoreForm,Fixturedetail,pointstable)

urlpatterns = [
    path('', test),
    path('homepage/', Index.as_view(), name = 'index'),
    path('pointstable/', pointstable.as_view(), name = 'pointstable'),
    path('teamdetails/', Teams.as_view(), name = 'teamlist'),
    path('fixtures/',Fixtures_Form.as_view(), name='fixtures'),
    path('fixtures/listoffixtures/',Fixtures.as_view(), name='fixtureslist'),
    path('fixtures/listoffixtures/<int:pk>/',Fixturedetail.as_view(), name='fixturedetail'),
    path('fixtures/listoffixtures/scoreupdate', ScoreForm.as_view(), name ='scoreupdate'),
    path('teamdetails/newteam', NewTeam.as_view(), name='newteam'),
    path('teamdetails/<int:pk>/', PlayerDetailView.as_view(), name='teamname'),
    path('teamdetails/newplayers/', NewPlayer.as_view(), name='newplayer'),
    path('teamdetails/<int:player_details_pk>/<int:pk>/', PlayerStatistics.as_view(), name= 'playerdetails'),
    path('teamdetails/<int:pk>/batstatistics', BatStatistics.as_view(), name= 'batstatistics'),
    path('teamdetails/<int:pk>/bowlstatistics', BowlStatistics.as_view(), name= 'bowlstatistics'),
    
    ]