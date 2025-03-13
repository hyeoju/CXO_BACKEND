from fastapi import FastAPI, File, UploadFile
from app.routes import rag, vector_db

app = FastAPI()
# 라우터 추가
app.include_router(rag.router, prefix="/rag", tags=["RAG"])
app.include_router(vector_db.router, prefix="/vector", tags=["Vector DB"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Vector DB API"}
@app.get("/")
def read_root():
    return {"message": "Welcome to the Q&A Backend!"}

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "content_type": file.content_type
    }

# 여러 파일을 동시에 업로드하는 예시
@app.post("/upload-multiple/")
async def upload_multiple_files(files: list[UploadFile] = File(...)):
    return [{"filename": file.filename} for file in files]
