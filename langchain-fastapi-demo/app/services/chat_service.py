from langchain_openai import ChatOpenAI
from app.config import settings

class ChatService:
    def __init__(self):
        self.llm = ChatOpenAI(
            model=settings.chat_model,
            api_key=settings.openai_api_key or None,
            base_url=settings.openai_base_url or None,
            temperature=0.2
        )

    def converse(self, question: str) -> str:
        res = self.llm.invoke(question)
        return res.content
