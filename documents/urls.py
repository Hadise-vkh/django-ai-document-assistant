from django.urls import path
from .views import (
    DocumentListAPIView,
    DocumentDetailAPIView,
    AskQuestionAPIView,
    QuestionHistoryListAPIView
)

urlpatterns = [
    path("", DocumentListAPIView.as_view()),
    path("<int:pk>/", DocumentDetailAPIView.as_view()),
    path("ask/", AskQuestionAPIView.as_view()),
    path("history/", QuestionHistoryListAPIView.as_view()),
]