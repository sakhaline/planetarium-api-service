import django_filters

from planetarium.models import AstronomyShow, ShowSession, ShowTheme


class AstronomyShowFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains")
    themes = django_filters.ModelMultipleChoiceFilter(
        queryset=ShowTheme.objects.all(),
        field_name="themes",
        label="Astronomy Show Theme",
    )

    class Meta:
        model = AstronomyShow
        fields = ["title", "themes"]


class ShowSessionFilter(django_filters.FilterSet):
    astronomy_show = django_filters.CharFilter(
        field_name="astronomy_show__title",
        lookup_expr="icontains",
        label="Astronomy Show Title",
    )

    show_time = django_filters.DateTimeFilter(
        field_name="show_time",
        lookup_expr="gte",
        label="Show Time (Greater Than or Equal To)",
    )

    class Meta:
        model = ShowSession
        fields = ["astronomy_show", "show_time"]
