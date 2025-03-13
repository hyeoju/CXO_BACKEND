import os
from dotenv import load_dotenv

load_dotenv()

# Chroma DB 설정
CHROMA_DB_DIR = "./chroma_db"

# HuggingFace 모델 설정
MODEL_NAME = "Qwen/Qwen2.5-Coder-3B-Instruct"

# OpenAI API 설정
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

HUGGINGFACE_TOKEN = os.getenv('HUGGINGFACE_TOKEN')

