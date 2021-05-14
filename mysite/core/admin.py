from django.contrib import admin
from .models import * # Lấy hết model đem vô đây

# Register your models here.
admin.site.register(Race)
admin.site.register(Racer)
admin.site.register(Bet)
