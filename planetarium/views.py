from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import HttpRequest

from planetarium.models import (ShowTheme,
                                AstronomyShow,
                                PlanetariumDome,
                                Reservation,
                                ShowSession,
                                Ticket,)
from planetarium.serializers import (ShowThemeSerializer,
                                     )


@api_view()
def show_theme_list(request: HttpRequest) -> Response:
    show_themes = ShowTheme.objects.all()
    serializer = ShowThemeSerializer(show_themes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
