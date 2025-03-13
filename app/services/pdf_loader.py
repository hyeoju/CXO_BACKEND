from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_and_split_pdf(file_path):
    loader = PyMuPDFLoader(file_path)
    docs = loader.load()
    
    # 텍스트 분할
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=50)
    split_documents = text_splitter.split_documents(docs)
    return split_documents
