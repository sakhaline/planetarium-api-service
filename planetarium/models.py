from django.core.exceptions import ValidationError
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
        to=ShowTheme,
        related_name="astronomy_shows",
    )

    def __str__(self):
        return self.title


class Reservation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return str(self.created_at)


class ShowSession(models.Model):
    astronomy_show = models.ForeignKey(
        to=AstronomyShow,
        related_name="show_sessions",
        on_delete=models.CASCADE,
    )
    planetarium_dome = models.ForeignKey(
        to=PlanetariumDome,
        related_name="show_sessions",
        on_delete=models.CASCADE,
    )
    show_time = models.DateTimeField()

    class Meta:
        ordering = ("astronomy_show", "planetarium_dome")

    @property
    def tickets_available(self):
        total_seats = self.planetarium_dome.rows * self.planetarium_dome.seats_in_row
        booked_tickets = self.tickets.count()
        return total_seats - booked_tickets

    def __str__(self):
        return self.astronomy_show.title + " " + str(self.show_time)


class Ticket(models.Model):
    row = models.IntegerField()
    seat = models.IntegerField()
    show_session = models.ForeignKey(
        to=ShowSession,
        related_name="tickets",
        on_delete=models.CASCADE,
    )
    reservation = models.ForeignKey(
        to=Reservation,
        related_name="tickets",
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = ("row", "seat", "show_session")

    @staticmethod
    def validate_ticket(row, seat, planetarium_dome, error_to_raise):
        for ticket_attr_value, ticket_attr_name, planetarium_dome_attr_name in [
            (row, "row", "rows"),
            (seat, "seat", "seats_in_row"),
        ]:
            count_attrs = getattr(planetarium_dome, planetarium_dome_attr_name)
            if not (1 <= ticket_attr_value <= count_attrs):
                raise error_to_raise(
                    {
                        ticket_attr_name: f"{ticket_attr_name} "
                        f"number must be in available range: "
                        f"(1, {planetarium_dome_attr_name}): "
                        f"(1, {count_attrs})"
                    }
                )

    def clean(self):
        Ticket.validate_ticket(
            self.row,
            self.seat,
            self.show_session.planetarium_dome,
            ValidationError,
        )

    def save(
        self,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):
        self.full_clean()
        return super(Ticket, self).save(
            force_insert, force_update, using, update_fields
        )

    def __str__(self):
        return f"{self.show_session}" f"row: {self.row}, seat: {self.seat}"
