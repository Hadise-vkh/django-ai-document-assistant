from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

response = client.embeddings.create(
    model="text-embedding-3-small",
    input="Hello world"
)

print(response.data[0].embedding[:5])