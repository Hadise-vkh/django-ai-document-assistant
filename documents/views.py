from openai import OpenAI
from dotenv import load_dotenv
import os

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Document, QuestionHistory
from .serializers import DocumentSerializer

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)


class DocumentListAPIView(generics.ListAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class AskQuestionAPIView(APIView):
    def post(self, request):
        question = request.data.get("question", "")

        documents = Document.objects.all()

        context = ""

        for doc in documents:
            context += doc.content + "\n"

        response = client.chat.completions.create(
            model="openrouter/free",
            messages=[
                {
                    "role": "system",
                    "content": "Answer questions only using the provided documents."
                },
                {
                    "role": "user",
                    "content": f"""
Documents:
{context}

Question:
{question}
"""
                }
            ]
        )

        answer = response.choices[0].message.content

        QuestionHistory.objects.create(
            question=question,
            answer=answer
        )

        return Response({
            "answer": answer
        })