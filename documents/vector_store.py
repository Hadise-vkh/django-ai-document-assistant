import os

from dotenv import load_dotenv
from openai import OpenAI

from langchain_chroma import Chroma
from langchain_core.embeddings import Embeddings
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()


class OpenRouterEmbeddings(Embeddings):
    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("OPENROUTER_API_KEY"),
            base_url="https://openrouter.ai/api/v1",
        )

    def embed_query(self, text):
        response = self.client.embeddings.create(
            model="text-embedding-3-small",
            input=text
        )

        return response.data[0].embedding

    def embed_documents(self, texts):
        return [
            self.embed_query(text)
            for text in texts
        ]


embedding_function = OpenRouterEmbeddings()

vector_store = Chroma(
    collection_name="documents",
    embedding_function=embedding_function,
    persist_directory="./chroma_db",
)

def add_document_to_vector_store(document_id, text):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_text(text)

    documents = [
        Document(
            page_content=chunk,
            metadata={
                "document_id": document_id
            }
        )
        for chunk in chunks
    ]

    vector_store.add_documents(documents)