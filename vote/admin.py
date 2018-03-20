from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Team)
admin.site.register(Vote)
admin.site.register(Voting)
admin.site.register(VotingPage)