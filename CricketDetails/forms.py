from django import forms
from CricketDetails.models import TeamStructure


class NewTeamForm(forms.ModelForm):
    class Meta:
        model = TeamStructure
        fields = '__all__'