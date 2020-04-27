from django.db import models
from django.core.validators import RegexValidator
from django.db.models import Sum, F, Max, Q
from django.urls import reverse
import pytz
import warnings


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


class Ground(models.Model):
    clubstate = models.ForeignKey('Clubstate', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.clubstate) + ' - ' + self.name

class MatchDate(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()
    date = models.DateField()

    def get_date(self):
        return date(self.year, self.month, self.day)

    def get_datetime(self):
        return datetime(self.year, self.month, self.day, 12, 0, 0, 0, pytz.UTC)

    def __str__(self):
        return str(self.year) + '/' + str(self.month) + '/' + str(self.day)



class Match(models.Model):
    
    date = models.ForeignKey('MatchDate', on_delete=models.CASCADE)
    ground = models.ForeignKey('Ground', on_delete=models.CASCADE)
    home_team = models.ForeignKey('TeamStructure', on_delete=models.CASCADE, related_name='home_team')
    away_team = models.ForeignKey('TeamStructure', on_delete=models.CASCADE, related_name='away_team')

    

    # Toss
    toss_won_by_team_id = models.CharField(max_length=8)
    toss = models.CharField(max_length=512)
    batted_first = models.CharField(max_length=8)

    # Result
    result = models.CharField(max_length=2)
    result_description = models.CharField(max_length=512)
    result_applied_to = models.CharField(max_length=8)
    match_notes = models.TextField()
    number_of_players = models.IntegerField(default=0)

    # Upload Status
    full_scorecard = models.BooleanField(default=False)
    processing_issue = models.BooleanField(default=False)

    # METHODS
    def match_description(self):
        ''' Creates a descriptive detail of the match '''
        warnings.warn('match_description not setup correctly', UserWarning)
        if True:  # self.home_team.club.pc_id == settings.PC_CLUB_ID:
            return self.home_team.name + ' vs ' + self.away_team.club.name + ' ' + self.away_team.name
        else:
            return self.away_team.name + ' vs ' + self.home_team.club.name + ' ' + self.home_team.name

    def is_live_score(self):
        return self.result == 'M'

    def __str__(self):
        # Gives useful info when using shell
        return str(self.home_team) + ': vs ' + self.opposition()

    def get_absolute_url(self):
        return reverse('matches:match', kwargs={'match_id': self.id})

    def opposition(self):
        warnings.warn('opposition not setup correctly', UserWarning)
        if True:  # self.home_team.club.pc_id == settings.PC_CLUB_ID:
            return str(self.away_team)
        else:
            return str(self.home_team)

    def site_team(self):
        warnings.warn('site_team not setup correctly', UserWarning)
        if True:  # self.home_team.club.pc_id == settings.PC_CLUB_ID:
            return self.home_team.name
        else:
            return self.away_team.name

    def innings(self):
        innings = Inning.objects.filter(match_id=self.id)
        if innings:
            return sorted(innings, key=lambda a: a.get_inning_no())
        else:
            return []


# Inning Model
# Used for storing information about each inning in a match.
# x2 linked to match
class Inning(models.Model):
    # Foreign Keys
    match = models.ForeignKey('Match', on_delete=models.CASCADE)

    # Fields
    bat_team = models.ForeignKey('TeamStructure', on_delete=models.CASCADE, related_name='bat_team')
    bowl_team = models.ForeignKey('TeamStructure', on_delete=models.CASCADE, related_name='bowl_team')

    runs = models.IntegerField()
    wickets = models.IntegerField()
    overs = models.FloatField()
    declared = models.BooleanField()
    extras_byes = models.IntegerField(default=0)
    extras_leg_byes = models.IntegerField(default=0)
    extras_wides = models.IntegerField(default=0)
    extras_no_balls = models.IntegerField(default=0)
    extras_penalties = models.IntegerField(default=0)
    extras_total = models.IntegerField(default=0)
    highlights = models.TextField(default='')
    complete_innings = models.BooleanField(default=False)
    inning_no = models.IntegerField(default=0)

    def __str__(self):
        return 'Inning ' + str(self.inning_no) + ': ' + str(self.match)


class PlayerStructure(models.Model):
    clubstate =  models.ForeignKey('Clubstate', on_delete=models.CASCADE,  related_name='clubstate')
    country = models.ForeignKey('TeamStructure', on_delete=models.CASCADE, null=True,  related_name='identifier1')
    firstname =  models.CharField(max_length=255)
    lastname  =  models.CharField(max_length=255)
    imageUri =   models.ImageField(upload_to='images/', verbose_name='image')
    JerseyNumber = models.IntegerField()
    BirthPlace = models.CharField(max_length=10,default=False)
    BirthDate = models.CharField(max_length=30,default=False)
    Role      = models.CharField(max_length= 20, default =False)
    BattingStyle = models.CharField(max_length= 20, default = False)
    BowlingStyle = models.CharField(max_length= 20, default = False)

    def __str__(self):
        return self.firstname + self.lastname


class BatPerformance(models.Model):
    # Foreign Keys
    match = models.ForeignKey('Match', on_delete=models.CASCADE, related_name = 'matchdetails')
    player = models.ForeignKey('PlayerStructure', on_delete=models.CASCADE, related_name = 'playerbatperf')

    # Batting Performance Fields
    batting_atches = models.IntegerField(default=0)
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
        return str(self.player) + ': ' + str(self.match)




class BowlPerformance(models.Model):
    # Foreign Keys
    match = models.ForeignKey('Match', on_delete=models.CASCADE)
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
        return str(self.player) + ': ' + str(self.match)



class FieldPerformance(models.Model):
    # Foreign Keys
    match = models.ForeignKey('Match', on_delete=models.CASCADE)
    player = models.ForeignKey('PlayerStructure', on_delete=models.CASCADE)

    # Fielding Performance Fields
    field_catches = models.IntegerField(default=0)
    field_run_outs = models.IntegerField(default=0)
    field_stumped = models.IntegerField(default=0)

    def __str__(self):
        return str(self.player) + ': ' + str(self.match)
