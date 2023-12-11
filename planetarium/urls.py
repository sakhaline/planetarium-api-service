from django.urls import path
from planetarium import views

app_name = "planetarium"

urlpatterns = [
    path("show_themes/", views.show_theme_list, name='index')
]