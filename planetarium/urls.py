from django.urls import path
from planetarium.views import (ShowThemeList,
                               ShowThemeDetail,
                               AstronomyShowList,
                               AstronomyShowDetail,
                               PlanetariumDomeList,
                               PlanetariumDomeDetail,)

app_name = "planetarium"

urlpatterns = [
    path("show_themes/", ShowThemeList.as_view(), name='show-theme-list'),
    path("show_themes/<int:pk>/", ShowThemeDetail.as_view(), name="show-theme-detail"),
    path("astronomy_shows/", AstronomyShowList.as_view(), name="astronomy-show-list"),
    path("astronomy_shows/<int:pk>/", AstronomyShowDetail.as_view(), name="astronomy-show-detail"),
    path("planetarium_domes/", AstronomyShowList.as_view(), name="planetarium-dome-list"),
    path("planetarium_domes/<int:pk>/", AstronomyShowDetail.as_view(), name="planetarium-dome-detail"),
]