from typing import List
from langchain_openai import OpenAIEmbeddings
from app.config import settings

class EmbedService:
    def __init__(self):
        self.emb = OpenAIEmbeddings(
            model=settings.embedding_model,
            api_key=settings.openai_api_key or None,
            base_url=settings.openai_base_url or None
        )

    def embed(self, text: str) -> list[float]:
        return self.emb.embed_query(text)

