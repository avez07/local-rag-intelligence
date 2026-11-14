from fastapi import FastAPI, UploadFile, File, HTTPException
from app.config import settings
from app.service.ollama import generate_response
from app.service.chat import ChatRequest, ChatResponse
from pathlib import Path
import shutil
from app.service.document import extract_text

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
)

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "environment": settings.app_env,
    }

@app.get("/test-llm")
async def test_llm():
    answer = await generate_response("Explain RAG in Two Sentences.")
    return {"answer": answer}

@app.post("/api/v1/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    answer = await generate_response(request.question)
    return ChatResponse(answer=answer)

@app.post("/api/v1/documents/upload")
async def upload_document(file: UploadFile = File(...)):
    file_path = UPLOAD_DIR / Path(file.filename).name

    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text(str(file_path))

    result = {
        "filename": file.filename,
        "characters_extracted": len(text),
        "preview": text[:500]
    }

    print("API RESPONSE:", result)

    return result