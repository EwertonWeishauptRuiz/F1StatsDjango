from django.contrib import admin
from f12018.models import (Driver, Race, Position, Country, Team)
# Register your models here.
admin.site.register(Driver)
admin.site.register(Race)
admin.site.register(Position)
admin.site.register(Country)
admin.site.register(Team)
