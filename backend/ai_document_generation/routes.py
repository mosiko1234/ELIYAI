from fastapi import APIRouter, HTTPException
import os
from .openai_client import OpenAIClient

router = APIRouter()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY is not set in the environment")

client = OpenAIClient(api_key=api_key)

@router.post("/generate-document")
async def generate_document(prompt: str):
    try:
        document = client.generate_document(prompt)
        return {"document": document}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
