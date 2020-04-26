from django.urls import path,include, re_path
from django.conf.urls import url

from CricketDetails.views import Teams,Index,NewTeam,PlayerDetailView,test

urlpatterns = [
    path('', test, name= 'test'),
    path('homepage/', Index.as_view(), name = 'index'),
    path('teamdetails/', Teams.as_view(), name = 'teamlist'),
    path('teamdetails/newteam', NewTeam.as_view(), name='newteam'),
    re_path(r'teamdetails/(?P<pk>\d+)/', PlayerDetailView.as_view(), name='teamname'),
    ]