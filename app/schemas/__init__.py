from fastapi import FastAPI
from app.config import settings
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.ollama import generate_response

app = FastAPI(title=settings.app_name, debug=settings.debug)


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/api/v1/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    answer = await generate_response(request.question)
    return ChatResponse(answer=answer)