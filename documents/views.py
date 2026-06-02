from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Document, QuestionHistory
from .serializers import (
    DocumentSerializer,
    QuestionHistorySerializer
)
from .vector_store import vector_store

load_dotenv()

llm = ChatOpenAI(
    model="openrouter/free",
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1",
)


class QuestionHistoryListAPIView(generics.ListAPIView):
    queryset = QuestionHistory.objects.all().order_by("-created_at")
    serializer_class = QuestionHistorySerializer



class DocumentListAPIView(generics.ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class DocumentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class AskQuestionAPIView(APIView):
    def post(self, request):
        question = request.data.get("question", "")

        results = vector_store.similarity_search(
            question,
            k=3
        )

        context = "\n\n".join(
            doc.page_content
            for doc in results
        )

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