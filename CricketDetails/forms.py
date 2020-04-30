from django import forms
from CricketDetails.models import TeamStructure,PlayerStructure,BatPerformance,BowlPerformance,Match,Score




class NewTeamForm(forms.ModelForm):
    class Meta:
        model = TeamStructure
        fields = '__all__'

        widgets={
            'identifier': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'summary': forms.TextInput(attrs={'class': 'form-control'})
        }


class NewPlayerForm(forms.ModelForm):
    class Meta:
        model = PlayerStructure
        fields = '__all__'

        widgets={

        'firstname' : forms.TextInput(attrs={'class': 'form-control'}),
        'lastname' : forms.TextInput(attrs={'class': 'form-control'}),
        'JerseyNumber' : forms.TextInput(attrs={'class': 'form-control'}),
        'BirthPlace' : forms.TextInput(attrs={'class': 'form-control'}),
        'BirthDate' : forms.TextInput(attrs={'class': 'form-control'}),
        'Role' : forms.TextInput(attrs={'class': 'form-control'}),
        'BattingStyle' : forms.TextInput(attrs={'class': 'form-control'}),
        'BowlingStyle' : forms.TextInput(attrs={'class': 'form-control'}),
        }

class NewPlayerBatStatistics(forms.ModelForm):
    class Meta:
        model = BatPerformance
        exclude = ('match',)

        widgets = {
            'batting_atches' : forms.NumberInput(attrs={'class': 'form-control'}),
            'batting_innings' : forms.NumberInput(attrs={'class': 'form-control'}),
            'batting_notouts': forms.NumberInput(attrs={'class': 'form-control'}),
            'batting_Runs' : forms.NumberInput(attrs={'class': 'form-control'}),
            'batting_HS' : forms.NumberInput(attrs={'class': 'form-control'}),
            'batting_avg' : forms.NumberInput(attrs={'class': 'form-control'}),
            'batting_ballsfaced' : forms.NumberInput(attrs={'class': 'form-control'}),
            'batting_hundreds'  : forms.NumberInput(attrs={'class': 'form-control'}),
            'batting_fifty'  : forms.NumberInput(attrs={'class': 'form-control'}),
            'batting_twohundreds'  : forms.NumberInput(attrs={'class': 'form-control'}),
            'batting_fours'  : forms.NumberInput(attrs={'class': 'form-control'}),
            'batting_sixes'  : forms.NumberInput(attrs={'class': 'form-control'})
        }

        
class NewPlayerBowlStatistics(forms.ModelForm):
    class Meta:
        model = BowlPerformance
        exclude = ('match',)

        widgets = {
            'bowl_matches'  : forms.NumberInput(attrs={'class': 'form-control'}),
            'bowl_innings'  : forms.NumberInput(attrs={'class': 'form-control'}),
            'bowl_noofballs'  : forms.NumberInput(attrs={'class': 'form-control'}),
            'bowl_runs'  : forms.NumberInput(attrs={'class': 'form-control'}),
            'bowl_wkts'  : forms.NumberInput(attrs={'class': 'form-control'}),
            'bowl_wickets_lbw'  : forms.NumberInput(attrs={'class': 'form-control'}),
            'bowl_wickets_economy'  : forms.NumberInput(attrs={'class': 'form-control'}),
            'bowl_wickets_stumped'  : forms.NumberInput(attrs={'class': 'form-control'}),
            'bowl_wickets_avgt'  : forms.NumberInput(attrs={'class': 'form-control'}),
            'bowl_wickets_SR'  : forms.NumberInput(attrs={'class': 'form-control'}),
            'bowl_five_wickets'  : forms.NumberInput(attrs={'class': 'form-control'}),
            'bowl_ten_wickets'  : forms.NumberInput(attrs={'class': 'form-control'})
                }

class FixturesForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = '__all__'

        widgets = {

            'ground'  : forms.TextInput(attrs={'class': 'form-control'}),
            'League'  : forms.TextInput(attrs={'class': 'form-control'})
                }

class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = '__all__'

        widgets = {

            'team1Score'  : forms.NumberInput(attrs={'class': 'form-control'}),
            'team2Score'  : forms.NumberInput(attrs={'class': 'form-control'})
                }
        