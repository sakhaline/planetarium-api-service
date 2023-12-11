from django.db import transaction
from django.http import Http404
from rest_framework import serializers

from planetarium.models import (ShowTheme,
                                PlanetariumDome,
                                AstronomyShow,
                                Reservation,
                                ShowSession,
                                Ticket,)


class ShowThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowTheme
        fields = ["id", "name"]


class PlanetariumDomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanetariumDome
        fields = ["id", "name", "rows", "seats_in_row"]


# class AstronomyShowSerializer(serializers.ModelSerializer):
#     themes = serializers.ListSerializer(child=serializers.IntegerField())
#
#     class Meta:
#         model = AstronomyShow
#         fields = ["id", "title", "description", "themes"]
#
#     def create(self, validated_data):
#         themes = validated_data.pop("themes")
#         astronomy_show = AstronomyShow.objects.create(**validated_data)
#
#         for theme_id in themes:
#             try:
#                 theme = ShowTheme.objects.get(pk=theme_id)
#                 astronomy_show.themes.add(theme)
#             except:
#                 raise Http404(f"ShowTheme with ID {theme_id} does not exist.")
#
#         return astronomy_show
#
#     def update(self, instance, validated_data):
#         themes = validated_data.pop("themes")
#
#         instance.title = validated_data.get("title", instance.title)
#         instance.description = validated_data.get("description", instance.description)
#         instance.save()
#
#         for theme_id in themes:
#             try:
#                 theme = ShowTheme.objects.get(pk=theme_id)
#                 instance.themes.add(theme)
#             except:
#                 raise Http404(f"ShowTheme with ID {theme_id} does not exist.")
#
#         return instance
#
#
# class AstronomyShowListSerializer(AstronomyShowSerializer):
#     themes = serializers.SlugRelatedField(
#         many=True,
#         read_only=True,
#         slug_field="name"
#     )
#     class Meta:
#         model = AstronomyShow
#         fields = ["id", "title", "description", "themes"]


class AstronomyShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = AstronomyShow
        fields = ["id", "title", "description", "themes"]


class AstronomyShowListSerializer(serializers.ModelSerializer):
    themes = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name",
    )
    class Meta:
        model = AstronomyShow
        fields = ["id", "title", "description", "themes"]


class AstronomyShowDetailSerializer(serializers.ModelSerializer):
    themes = ShowThemeSerializer(read_only=True, many=True)
    class Meta:
        model = AstronomyShow
        fields = ["id", "title", "description", "themes"]


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ["id", "created_at", "user"]


class ShowSessionSerializer(serializers.ModelSerializer):
    astronomy_show = AstronomyShowSerializer()
    planetarium_dome = PlanetariumDomeSerializer()
    class Meta:
        model = ShowSession
        fields = [
            "id",
            "astronomy_show",
            "planetarium_dome",
            "show_time",
        ]


class ShowSessionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowSession
        fields = [
            "id",
            "astronomy_show",
            "planetarium_dome",
            "show_time",
        ]

class TicketSerializer(serializers.ModelSerializer):
    show_session = ShowSessionSerializer()
    reservation = ReservationSerializer()
    class Meta:
        model = Ticket
        fields = [
            "id",
            "row",
            "seat",
            "show_session",
            "reservation",
        ]


class TicketListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = [
            "id",
            "row",
            "seat",
            "show_session",
            "reservation",
        ]