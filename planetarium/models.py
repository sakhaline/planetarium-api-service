from django.db import models

from planetarium_config import settings


class ShowTheme(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class PlanetariumDome(models.Model):
    name = models.CharField(max_length=50)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    @property
    def capacity(self) -> int:
        return self.rows * self.seats_in_row

    def __str__(self):
        return self.name


class AstronomyShow(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    themes = models.ManyToManyField(
        to=ShowTheme, related_name="astronomy_shows",
    )

    def __str__(self):
        return self.title


class Reservation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return str(self.created_at)


class ShowSession(models.Model):
    astronomy_show = models.ForeignKey(
        to=AstronomyShow, related_name="show_sessions", on_delete=models.CASCADE,
    )
    planetarium_dome = models.ForeignKey(
        to=PlanetariumDome, related_name="show_sessions", on_delete=models.CASCADE,
    )
    show_time = models.DateTimeField()

    class Meta:
        ordering = ("astronomy_show", "planetarium_dome")

    def __str__(self):
        return self.astronomy_show.title + " " + str(self.show_time)


class Ticket(models.Model):
    row = models.IntegerField()
    seat = models.IntegerField()
    show_session = models.ForeignKey(
        to=ShowSession, related_name="tickets", on_delete=models.CASCADE,
    )
    reservation = models.ForeignKey(
        to=Reservation, related_name="tickets", on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = ("row", "seat", "show_session")

    def __str__(self):
        return f"{self.show_session}"\
               f"row: {self.row}, seat: {self.seat}"

