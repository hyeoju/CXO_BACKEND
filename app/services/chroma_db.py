import os
import chromadb
from chromadb.config import Settings
from langchain_community.embeddings import HuggingFaceEmbeddings
from huggingface_hub import login
from app.config import HUGGINGFACE_TOKEN
# 환경변수에서 토큰 가져오기
login(token=HUGGINGFACE_TOKEN)

# embeddings 객체를 전역 변수로 생성
embeddings = HuggingFaceEmbeddings(
    model_name='jhgan/ko-sroberta-multitask',
    model_kwargs={'device':'cpu'},
    encode_kwargs={'normalize_embeddings':True},
)

def get_chroma_client():
    try:
        # 새로운 방식으로 ChromaDB 클라이언트 생성
        client = chromadb.PersistentClient(
            path="./chroma_db"  # 데이터를 저장할 경로
        )
        return client
    except Exception as e:
        raise Exception(f"ChromaDB 클라이언트 생성 실패: {str(e)}")

def add_to_chroma(client, documents):
    try:
        collection = client.get_or_create_collection("my_collection")
        # documents를 텍스트와 임베딩으로 변환
        texts = [doc.page_content for doc in documents]
        embeddings_list = embeddings.embed_documents(texts)
        # add 메서드 사용
        collection.add(
            embeddings=embeddings_list,
            documents=texts,
            ids=[str(i) for i in range(len(texts))]  # 각 문서에 대한 고유 ID 생성
        )
        return {"message": "Documents added successfully"}
    except Exception as e:
        raise Exception(f"문서 추가 실패: {str(e)}")

def search_chroma(client, query, top_k=5):
    try:
        collection = client.get_collection("my_collection")
        query_embedding = embeddings.embed_query(query)
        results = collection.query(
            query_embeddings=[query_embedding], 
            n_results=top_k
        )
        # results['documents'][0]에 검색된 문서들의 리스트가 있습니다
        return {
            "documents": results['documents'][0],  # 첫 번째 쿼리의 결과만 반환
            "distances": results['distances'][0]   # 유사도 점수도 함께 반환
        }
    except Exception as e:
        raise Exception(f"검색 실패: {str(e)}")