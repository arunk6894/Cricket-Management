from django import forms
from CricketDetails.models import TeamStructure,PlayerStructure



class NewTeamForm(forms.ModelForm):
    class Meta:
        model = TeamStructure
        fields = '__all__'


class NewPlayerForm(forms.ModelForm):
    class Meta:
        model = PlayerStructure
        fields = '__all__'