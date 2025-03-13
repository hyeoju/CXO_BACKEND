from fastapi import APIRouter, HTTPException
from app.services.model_loader import load_model
from app.services.chroma_db import get_chroma_client, search_chroma

router = APIRouter()
model_pipeline = load_model()
client = get_chroma_client()

    @router.post("/query")
def query_rag(question: str):
    model, tokenizer = model_pipeline  # 튜플 언패킹
    
    prompt = f"Question: {question}\nAnswer:"
    
    # 모델 추론 실행
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(
        **inputs,
        max_length=2048,
        temperature=0.7,
        num_return_sequences=1
    )
    
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"response": response}
