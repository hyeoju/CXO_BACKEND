from fastapi import APIRouter, UploadFile, HTTPException
import os
from app.services.pdf_loader import load_and_split_pdf
from app.services.chroma_db import add_to_chroma, get_chroma_client

router = APIRouter()
client = get_chroma_client()  # Chroma DB 클라이언트 초기화

@router.post("/upload")
async def upload_pdf(file: UploadFile):
    # 업로드 경로 확인 및 생성
    upload_dir = "./uploads"
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)  # 디렉토리 생성

    # 파일 저장
    file_path = os.path.join(upload_dir, file.filename)
    try:
        with open(file_path, "wb") as f:
            f.write(await file.read())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save file: {e}")

    # 이후 처리 로직 (PDF 로드 및 벡터 추가)
    documents = load_and_split_pdf(file_path)
    response = add_to_chroma(client, documents)
    return response
