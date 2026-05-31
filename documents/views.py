from django.shortcuts import render
from rest_framework import generics
from .models import Document
from .serializers import DocumentSerializer


class DocumentListAPIView(generics.ListAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer