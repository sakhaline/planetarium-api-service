from django.contrib import admin

from planetarium import models


admin.site.register(models.ShowTheme)
admin.site.register(models.AstronomyShow)
admin.site.register(models.PlanetariumDome)
admin.site.register(models.Reservation)
admin.site.register(models.ShowSession)
admin.site.register(models.Ticket)
