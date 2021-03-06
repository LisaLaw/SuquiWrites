from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("entry/<int:pk>/", views.entry_detail, name="entry_detail"),
    path("entry/new/", views.entry_new, name="entry_new"),
    path("entry/<int:pk>/edit/", views.entry_edit, name="entry_edit"),
    # path("entry/<int:pk>/comment/", views.add_comment, name="add_comment"),
]
