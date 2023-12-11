from django.db import transaction
from rest_framework import serializers

from planetarium.models import ShowTheme, PlanetariumDome, AstronomyShow


class ShowThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowTheme
        fields = ["id", "name"]


class PlanetariumDomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanetariumDome
        fields = ["id", "name", "rows", "seats_in_row"]


class AstronomyShowListSerializer(serializers.ModelSerializer):
    themes = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )
    class Meta:
        model = AstronomyShow
        fields = ["id", "title", "description", "themes"]


class AstronomyShowSerializer(serializers.ModelSerializer):
    themes = ShowThemeSerializer(many=True, read_only=True)

    class Meta:
        model = AstronomyShow
        fields = ["id", "title", "description", "themes"]