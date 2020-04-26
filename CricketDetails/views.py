from django.shortcuts import render
from .models import BatPerformance, TeamStructure
from CricketDetails.forms import NewTeamForm
from django.http import HttpResponseRedirect
from django.views.generic import View, TemplateView, FormView, ListView, DetailView
from . import models
# Create your views here.



def test(request):
    return render(request,'test.html')

class Index(View):
    def get(self, request):
        return render(request, 'base.html')
    
class Teams(ListView):
    context_object_name = 'teams'
    model = models.TeamStructure
           

class NewTeam(FormView):
    template_name = 'teamform.html'
    form_class = NewTeamForm
    success_url = '.'

    def form_valid(self, form):
        # Form is Valid
        new_team = form.save(commit=True)
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        # Form is Invalid
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))


class PlayerDetailView(DetailView):
    context_object_name = 'player_details'
    model = models.TeamStructure
    template_name = 'CricketDetails/player_detail.html'

