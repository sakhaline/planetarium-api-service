from django.http import Http404
from rest_framework import status
from rest_framework.response import Response

from rest_framework.views import APIView

from planetarium.models import (ShowTheme,
                                AstronomyShow,
                                PlanetariumDome,
                                Reservation,
                                ShowSession,
                                Ticket,)
from planetarium.serializers import (ShowThemeSerializer,
                                     PlanetariumDomeSerializer,
                                     AstronomyShowListSerializer,
                                     AstronomyShowDetailSerializer,
                                     AstronomyShowSerializer,
                                     ReservationSerializer,
                                     ShowSessionSerializer,
                                     ShowSessionListSerializer,
                                     ShowSessionDetailSerializer,
                                     TicketSerializer,
                                     TicketListSerializer,)


class TicketList(APIView):
    def get(self, request):
        tickets = Ticket.objects.all()
        serializer = TicketListSerializer(tickets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TicketListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TicketDetail(APIView):
    def get_object(self, pk):
        try:
            return Ticket.objects.get(pk=pk)
        except Ticket.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        ticket = self.get_object(pk)
        serializer = TicketSerializer(ticket)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        ticket = self.get_object(pk)
        serializer = TicketSerializer(ticket, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        ticket = self.get_object(pk)
        serializer = TicketSerializer(ticket, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        ticket = self.get_object(pk)
        ticket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ShowSessionList(APIView):
    def get(self, request):
        show_sessions = ShowSession.objects.all()
        serializer = ShowSessionListSerializer(show_sessions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ShowSessionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShowSessionDetail(APIView):
    def get_object(self, pk):
        try:
            return ShowSession.objects.get(pk=pk)
        except ShowSession.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        show_session = self.get_object(pk)
        serializer = ShowSessionDetailSerializer(show_session)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        show_session = self.get_object(pk)
        serializer = ShowSessionSerializer(show_session, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        show_session = self.get_object(pk)
        serializer = ShowSessionSerializer(show_session, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        show_session = self.get_object(pk)
        show_session.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReservationList(APIView):
    def get(self, request):
        reservations = Reservation.objects.all()
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReservationDetail(APIView):
    def get_object(self, pk):
        try:
            return Reservation.objects.get(pk=pk)
        except Reservation.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        reservation = self.get_object(pk)
        serializer = ReservationSerializer(reservation)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        reservation = self.get_object(pk)
        serializer = ReservationSerializer(reservation, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        reservation = self.get_object(pk)
        serializer = ReservationSerializer(reservation, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        reservation = self.get_object(pk)
        reservation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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


class AstronomyShowList(APIView):
    def get(self, request):
        astronomy_shows = AstronomyShow.objects.all()
        serializer = AstronomyShowListSerializer(astronomy_shows, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AstronomyShowSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AstronomyShowDetail(APIView):
    def get_object(self, pk):
        try:
            return AstronomyShow.objects.get(pk=pk)
        except AstronomyShow.DoesNotExist:
            return Http404

    def get(self, request, pk):
        astronomy_show = self.get_object(pk=pk)
        serializer = AstronomyShowDetailSerializer(astronomy_show)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        astronomy_show = self.get_object(pk=pk)
        serializer = AstronomyShowSerializer(astronomy_show, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        astronomy_show = self.get_object(pk=pk)
        serializer = AstronomyShowSerializer(astronomy_show, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        astronomy_show = self.get_object(pk=pk)
        astronomy_show.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PlanetariumDomeList(APIView):
    def get(self, request):
        planetarium_domes = PlanetariumDome.objects.all()
        serializer = PlanetariumDomeSerializer(planetarium_domes, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def post(self, request):
        serializer = PlanetariumDomeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlanetariumDomeDetail(APIView):
    def get_object(self, pk):
        try:
            return PlanetariumDome.objects.get(pk=pk)
        except PlanetariumDome.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        planetarium_dome = self.get_object(pk=pk)
        serializer = PlanetariumDomeSerializer(planetarium_dome)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        planetarium_dome = self.get_object(pk=pk)
        serializer = PlanetariumDomeSerializer(planetarium_dome, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, pk):
        planetarium_dome = self.get_object(pk=pk)
        serializer = PlanetariumDomeSerializer(planetarium_dome, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        planetarium_dome = self.get_object(pk=pk)
        planetarium_dome.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



