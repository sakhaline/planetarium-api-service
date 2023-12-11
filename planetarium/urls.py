from django.urls import path
from planetarium.views import ShowThemeList, ShowThemeDetail

app_name = "planetarium"

urlpatterns = [
    path("show_themes/", ShowThemeList.as_view(), name='show-theme-list'),
    path("show_themes/<int:pk>/", ShowThemeDetail.as_view(), name="show-theme-detail")
]