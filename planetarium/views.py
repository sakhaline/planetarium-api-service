from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.views import APIView

from planetarium.models import (ShowTheme,
                                AstronomyShow,
                                PlanetariumDome,
                                Reservation,
                                ShowSession,
                                Ticket,)
from planetarium.serializers import (ShowThemeSerializer,
                                     PlanetariumDomeSerializer)


class ShowThemeList(APIView):
    def get(self, request):
        show_themes = ShowTheme.objects.all()
        serializer = ShowThemeSerializer(show_themes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ShowThemeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShowThemeDetail(APIView):
    def get_object(self, pk):
        try:
            return ShowTheme.objects.get(pk=pk)
        except ShowTheme.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        show_theme = self.get_object(pk)
        serializer = ShowThemeSerializer(show_theme)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        show_theme = self.get_object(pk)
        serializer = ShowThemeSerializer(show_theme, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        show_theme = self.get_object(pk)
        serializer = ShowThemeSerializer(show_theme, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        show_theme = self.get_object(pk)
        show_theme.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PlanetariumDomeList(APIView):
    def get(self, request):
        planetarium_dome = PlanetariumDome.objects.all()
        serializer = PlanetariumDomeSerializer(planetarium_dome, many=True)
        return Response(serializer, status=status.HTTP_201_CREATED)

    def post(self, request):
        serializer = PlanetariumDomeSerializer(request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PlanetariumDomeDetail(APIView):
    def get_object(self, pk):
        try:
            return PlanetariumDome.objects.get(pk=pk)
        except PlanetariumDome.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        planetarium_dome = self.get_object(pk)
        serializer = PlanetariumDomeSerializer(planetarium_dome)
        return Response(serializer, status=status.HTTP_200_OK)

    def put(self, request, pk):
        planetarium_dom = self.get_object(pk)
        serializer = PlanetariumDomeSerializer(planetarium_dom, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        planetarium_dome = self.get_object(pk)
        serializer = PlanetariumDomeSerializer(planetarium_dome, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        planetarium_dome = self.get_object()
        planetarium_dome.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



