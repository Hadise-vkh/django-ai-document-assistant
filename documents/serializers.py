from rest_framework import serializers
from .models import Document, QuestionHistory

class DocumentSerializer(serializers.ModelSerializer):
    file = serializers.FileField(required=False)

    class Meta:
        model = Document
        fields = "__all__"


class QuestionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionHistory
        fields = "__all__"