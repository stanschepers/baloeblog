from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Schacht)
admin.site.register(Vote)
admin.site.register(Por)
admin.site.register(VotingPage)