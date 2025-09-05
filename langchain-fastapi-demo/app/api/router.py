from fastapi import APIRouter, HTTPException
from app.models.chat import ChatRequest, ChatResponse
from app.models.embed import (EmbedRequest, EmbedResponse)
from app.services.chat_service import ChatService
from app.services.embed_service import EmbedService

router = APIRouter()

chat_service = ChatService()
embed_service = EmbedService()

@router.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    if not req.question:
        raise HTTPException(status_code=400, detail="question is required")
    answer = chat_service.converse(req.question)
    return ChatResponse(answer=answer)

@router.post("/embed", response_model=EmbedResponse)
def embed(req: EmbedRequest):
    vector = embed_service.embed(req.text)
    return EmbedResponse(vector=vector)
