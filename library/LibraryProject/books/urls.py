from django.urls import path
from .views import *


urlpatterns = [
  path("book",BookView.as_view()),
  path("book/<int:pk>",BookView.as_view()),
]
