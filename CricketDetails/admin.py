from django.contrib import admin
from CricketDetails.models import (Clubstate,TeamStructure,Match,
PlayerStructure,BatPerformance,BowlPerformance,Score,PointsTable)

# Register your models here.


admin.site.register(Clubstate)
admin.site.register(TeamStructure)
admin.site.register(PlayerStructure)
admin.site.register(Match)
admin.site.register(BatPerformance)
admin.site.register(BowlPerformance)
admin.site.register(Score)
admin.site.register(PointsTable)
