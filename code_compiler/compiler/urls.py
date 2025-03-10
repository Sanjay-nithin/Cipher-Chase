from django.urls import path
from . import views

urlpatterns = [
    path("level/<int:level>/question/<int:question>/", views.question_page, name="question"),
    path("play/", views.unity_game, name="game"),
    path("unity-button/", views.unity_button, name='unity_button'),
    path("track-tab-switch/", views.track_tab_switch, name="track_tab_switch"),
    path("get-progress/", views.get_progress, name="get_progress"),
]