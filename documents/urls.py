from django.urls import path
from .views import (
    DocumentListAPIView,
    AskQuestionAPIView
)

urlpatterns = [
    path("", DocumentListAPIView.as_view()),
    path("ask/", AskQuestionAPIView.as_view()),
]