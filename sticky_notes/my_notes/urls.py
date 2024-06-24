# my_notes/urls.py

from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="my_notes\login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="my_notes\home.html"),
        name="logout",
    ),
    path("signup/", views.signup, name="signup"),
    path("create_note/", views.create_note, name="create"),
    path("view/", views.view_notes, name="view"),
    path("notes/<int:note_id>/", views.check_note, name="check"),
    path("notes/<int:note_id>/edit/", views.edit_note, name="edit"),
    path("notes/<int:note_id>/delete/", views.delete_note, name="delete"),
    path("profile/", views.profile, name="user_profile"),
]
