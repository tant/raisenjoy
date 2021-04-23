from django.contrib import admin
from .models import Race, Racer, Wager, Bet


# Register your models here.
admin.site.register(Race)
admin.site.register(Racer)
admin.site.register(Wager)
admin.site.register(Bet)
