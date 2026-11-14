import httpx
from app.config import settings

async def generate_response(prompt: str):
    url = f"{settings.ollama_base_url}/api/generate"
    payload ={
        "model": settings.ollama_model,
        "prompt": prompt,
        "stream": False
    }

    async with httpx.AsyncClient(timeout=120) as client:
        response = await client.post(url,json=payload)
        response.raise_for_status()
        return response.json()["response"]