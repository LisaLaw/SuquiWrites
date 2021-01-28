from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("entry/<int:pk>/", views.entry_detail, name="entry_detail"),
]
