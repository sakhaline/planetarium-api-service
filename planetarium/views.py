from django.http import Http404
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from planetarium.filters import AstronomyShowFilter, ShowSessionFilter
from planetarium.models import (
    AstronomyShow,
    PlanetariumDome,
    Reservation,
    ShowSession,
    ShowTheme,
)

from planetarium.permissions import IsAdminOrIfAuthenticatedReadOnly
from planetarium.serializers import (
    AstronomyShowDetailSerializer,
    AstronomyShowListSerializer,
    AstronomyShowSerializer,
    PlanetariumDomeSerializer,
    ReservationListSerializer,
    ReservationSerializer,
    ShowSessionDetailSerializer,
    ShowSessionListSerializer,
    ShowSessionSerializer,
    ShowThemeSerializer,
)


class ShowSessionList(generics.ListCreateAPIView):
    queryset = ShowSession.objects.select_related(
        "astronomy_show", "planetarium_dome"
    )
    serializer_class = ShowSessionListSerializer
    filterset_class = ShowSessionFilter
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ShowSessionListSerializer
        elif self.request.method == "POST":
            return ShowSessionSerializer
        return ShowSessionListSerializer

    def post(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShowSessionDetail(APIView):
    permission_classes = (IsAuthenticated,)

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
        serializer = ShowSessionSerializer(
            show_session, data=request.data, partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        show_session = self.get_object(pk)
        show_session.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReservationList(APIView):
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)

    def get(self, request, *args, **kwargs):
        reservations = Reservation.objects.prefetch_related(
            "tickets__show_session__astronomy_show",
            "tickets__show_session__planetarium_dome",
        ).filter(user=request.user)

        serializer = ReservationListSerializer(reservations, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReservationDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Reservation.objects.get(pk=pk, user=self.request.user)
        except Reservation.DoesNotExist:
            raise Http404

    def get(self, request, pk, *args, **kwargs):
        reservation = self.get_object(pk)
        serializer = ReservationSerializer(reservation)
        return Response(serializer.data)


class ShowThemeList(APIView):
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)

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
    permission_classes = (IsAuthenticated,)

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
        serializer = ShowThemeSerializer(
            show_theme, data=request.data, partial=True,
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        show_theme = self.get_object(pk)
        show_theme.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AstronomyShowList(generics.ListCreateAPIView):
    queryset = AstronomyShow.objects.prefetch_related("themes")
    serializer_class = AstronomyShowListSerializer
    filterset_class = AstronomyShowFilter
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return AstronomyShowListSerializer
        elif self.request.method == "POST":
            return AstronomyShowSerializer
        return AstronomyShowListSerializer

    def post(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AstronomyShowDetail(APIView):
    permission_classes = (IsAuthenticated,)

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
        serializer = AstronomyShowSerializer(
            astronomy_show, data=request.data, partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        astronomy_show = self.get_object(pk=pk)
        astronomy_show.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PlanetariumDomeList(APIView):
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)

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
    permission_classes = (IsAuthenticated,)

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
        serializer = PlanetariumDomeSerializer(
            planetarium_dome, data=request.data,
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        planetarium_dome = self.get_object(pk=pk)
        serializer = PlanetariumDomeSerializer(
            planetarium_dome, data=request.data, partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        planetarium_dome = self.get_object(pk=pk)
        planetarium_dome.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
