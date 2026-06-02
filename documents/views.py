from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Document, QuestionHistory
from .serializers import DocumentSerializer

load_dotenv()

llm = ChatOpenAI(
    model="openrouter/free",
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1",
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

        prompt = f"""
Answer questions only using the provided documents.

Documents:
{context}

Question:
{question}
"""

        response = llm.invoke(prompt)

        answer = response.content

        QuestionHistory.objects.create(
            question=question,
            answer=answer
        )

        return Response({
            "answer": answer
        })