from transformers import GPT2Tokenizer
model_name_or_path = "sberbank-ai/rugpt3large_based_on_gpt2"
TOKENIZER = GPT2Tokenizer.from_pretrained(model_name_or_path)