from django.urls import path
from movieapp.api.views import movie

urlpatterns = [
    path("", movie , name="list movies")
]
