from django.db import models
from django.core.validators import RegexValidator
from django.urls import reverse
from django.db.models import Count


# Python Imports
from datetime import date, datetime
# Create your models here.


class Clubstate(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class TeamStructure(models.Model):
    clubstate =  models.ForeignKey('Clubstate', on_delete=models.CASCADE)
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    identifier =   models.CharField(max_length=50, blank=True, null=True, validators=[alphanumeric])
    name = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    logo1 = models.ImageField(upload_to='images/', verbose_name='logo1')
    logo2 = models.ImageField(upload_to='images/', verbose_name='logo2')
    logo3 = models.ImageField(upload_to='images/', verbose_name='logo3')
   

    def __str__(self):
        return self.name




class Match(models.Model):
    Bat_Bowl =(('Bat', 'Bat'), ('Bat', 'Bowl'))
    
    clubstate =  models.ForeignKey('Clubstate', on_delete=models.CASCADE, default=0)
    date = models.DateTimeField(default=datetime.now, blank= False)
    ground = models.CharField(max_length=100)
    Team1 = models.ForeignKey('TeamStructure', on_delete=models.CASCADE, related_name='team1',default = 0)
    Team2 = models.ForeignKey('TeamStructure', on_delete=models.CASCADE, related_name='team2',default = 0)
    Team1logo= models.ImageField(upload_to='images/', verbose_name = 'Team1 logo',default = 0)
    Team2logo= models.ImageField(upload_to='images/', verbose_name ='Team2 logo',default =0)
    League = models.CharField(max_length=100, default = 0)
    Toss_won_by =  models.ForeignKey('TeamStructure', on_delete=models.CASCADE, related_name='tosswon',default = 0)
    Elected_to = models.CharField(max_length=100,choices=Bat_Bowl) 

    def __str__(self):
        return str(self.Team1) + '  vs  ' + str(self.Team2) + ' Dated on ' + str(self.date.date()) +' at ' + str(self.ground)
    
    

    def toss_won(self):
        return 'Toss Won by ' + str(self.Toss_won_by) + ' and elected to ' +  str(self.Elected_to) + ' first'

class Score(models.Model):

    matches_between = models.ForeignKey('Match',on_delete = models.CASCADE, related_name ='fixture_between')
    Team1 = models.ForeignKey('TeamStructure', on_delete=models.CASCADE, related_name='teamA',default = 0)
    Team2 = models.ForeignKey('TeamStructure', on_delete=models.CASCADE, related_name='teamB',default = 0)
    team1Score = models.IntegerField(default = 0)
    team2Score = models.IntegerField(default = 0)

    def runs_gap(self):
        if self.team1Score > self.team2Score:
            return str(self.Team1) + ' won by ' +  str(self.team1Score - self.team2Score) + ' runs '
        else:
            return str(self.Team2) + ' won by ' + str(self.team2Score - self.team1Score) + ' runs '

    def team1_count(self): 
        team_count1 = {i["Team1"]: i["count"] for i in order_items.objects.values('Team1').order_by().annotate(count=Count('Team1'))}
        return team_count1
    
    def team2_count(self):
        team_count2 = {i["Team1"]: i["count"] for i in order_items.objects.values('Team2').order_by().annotate(count=Count('Team2'))}
        return team_count2

    def __str__(self):
        if self.team1Score > self.team2Score:
           return str(self.Team1)
        else:
            return str(self.Team2)
        
        
class PointsTable(models.Model):
    country = models.ForeignKey('TeamStructure', on_delete=models.CASCADE, null=True,  related_name='cont')
    team_won = models.ForeignKey('Score', on_delete=models.CASCADE, null=True,  related_name='won')


    def points_to_team(self):
        points={}
        points['team_won'] = 0
        if self.country == self.team_won:
            points[team_won] += 1
            return points

    







    



class PlayerStructure(models.Model):
    clubstate =  models.ForeignKey('Clubstate', on_delete=models.CASCADE,  related_name='clubstate')
    country = models.ForeignKey('TeamStructure', on_delete=models.CASCADE, null=True,  related_name='identifier1')
    firstname =  models.CharField(max_length=255)
    lastname  =  models.CharField(max_length=255)
    imageUri =   models.ImageField(upload_to='images/', verbose_name='image')
    JerseyNumber = models.IntegerField()
    BirthPlace = models.CharField(max_length=10)
    BirthDate = models.CharField(max_length=30)
    Role      = models.CharField(max_length= 20)
    BattingStyle = models.CharField(max_length= 20)
    BowlingStyle = models.CharField(max_length= 20)

    def __str__(self):
        return self.firstname + self.lastname


class BatPerformance(models.Model):
    # Foreign Keys
    country = models.ForeignKey('TeamStructure', on_delete=models.CASCADE, null=True,  related_name='country')
    player = models.ForeignKey('PlayerStructure', on_delete=models.CASCADE, related_name = 'playerbatperf')

    # Batting Performance Fields
    batting_Matches = models.IntegerField(default=0)
    batting_innings = models.IntegerField(default=0)
    batting_notouts = models.IntegerField(default=0)
    batting_Runs = models.IntegerField(default=0)
    batting_HS = models.IntegerField(default=0)
    batting_avg = models.FloatField(default=0.0)
    batting_ballsfaced = models.IntegerField(default=0)
    batting_strikerate = models.FloatField(default=0)
    batting_hundreds = models.IntegerField(default=0)
    batting_fifty = models.IntegerField(default=0)
    batting_twohundreds = models.IntegerField(default=0)
    batting_fours = models.IntegerField(default=0)
    batting_sixes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.player)




class BowlPerformance(models.Model):
    # Foreign Keys
    country = models.ForeignKey('TeamStructure', on_delete=models.CASCADE, null=True,  related_name='country1')

    player = models.ForeignKey('PlayerStructure', on_delete=models.CASCADE, related_name = 'playerbowlperf')

    # Bowling Performance Fields
    bowl_matches = models.FloatField(default=0)
    bowl_innings = models.IntegerField(default=0)
    bowl_noofballs = models.IntegerField(default=0)
    bowl_runs = models.IntegerField(default=0)
    bowl_wkts = models.IntegerField(default=0)
    bowl_wickets_lbw = models.IntegerField(default=0)
    bowl_wickets_economy = models.IntegerField(default=0)
    bowl_wickets_stumped = models.IntegerField(default=0)
    bowl_wickets_avgt = models.IntegerField(default=0)
    bowl_wickets_SR = models.IntegerField(default=0)
    bowl_five_wickets = models.IntegerField(default=0)
    bowl_ten_wickets = models.IntegerField(default=0)

    def __str__(self):
        return str(self.player)



