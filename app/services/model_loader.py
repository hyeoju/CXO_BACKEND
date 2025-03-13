from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

def load_model():
    # CPU에서는 float32를 사용
    model = AutoModelForCausalLM.from_pretrained(
        "Qwen/Qwen2.5-3B-Instruct",
        device_map="auto",
        torch_dtype=torch.float32,  # float16 대신 float32 사용
        low_cpu_mem_usage=True
    )
    
    tokenizer = AutoTokenizer.from_pretrained(
        "Qwen/Qwen2.5-3B-Instruct",
        trust_remote_code=True
    )
    
    return model, tokenizer
