from django.urls import path
from planetarium.views import (ShowThemeList,
                               ShowThemeDetail,
                               AstronomyShowList,
                               AstronomyShowDetail,
                               PlanetariumDomeList,
                               PlanetariumDomeDetail,
                               ReservationList,
                               ReservationDetail,
                               ShowSessionList,
                               ShowSessionDetail,
                               TicketList,
                               TicketDetail,)

app_name = "planetarium"

urlpatterns = [
    path("show_themes/", ShowThemeList.as_view(), name='show-theme-list'),
    path("show_themes/<int:pk>/", ShowThemeDetail.as_view(), name="show-theme-detail"),
    path("astronomy_shows/", AstronomyShowList.as_view(), name="astronomy-show-list"),
    path("astronomy_shows/<int:pk>/", AstronomyShowDetail.as_view(), name="astronomy-show-detail"),
    path("planetarium_domes/", PlanetariumDomeList.as_view(), name="planetarium-dome-list"),
    path("planetarium_domes/<int:pk>/", PlanetariumDomeDetail.as_view(), name="planetarium-dome-detail"),
    path("reservations/", ReservationList.as_view(), name="reservation-list"),
    path("reservations/<int:pk>/", ReservationDetail.as_view(), name="reservation-detail"),
    path("show_sessions/", ShowSessionList.as_view(), name="show-session-list"),
    path("show_sessions/<int:pk>/", ShowSessionDetail.as_view(), name="show-session-detail"),
    path("tickets/", TicketList.as_view(), name="ticket-list"),
    path("tickets/<int:pk>/", TicketDetail.as_view(), name="ticket-detail"),
]