from django.contrib import admin
from CricketDetails.models import (Clubstate,TeamStructure,
Ground,MatchDate,Match,Inning,
PlayerStructure,BatPerformance,BowlPerformance,FieldPerformance)

# Register your models here.


admin.site.register(Clubstate)
admin.site.register(TeamStructure)
admin.site.register(PlayerStructure)
admin.site.register(Ground)
admin.site.register(MatchDate)
admin.site.register(Match)
admin.site.register(Inning)
admin.site.register(BatPerformance)
admin.site.register(BowlPerformance)
admin.site.register(FieldPerformance)
