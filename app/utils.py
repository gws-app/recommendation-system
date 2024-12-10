import re

def custom_tokenizer(text):
    tokens = re.split(r'[^a-zA-Z0-9]', text)
    tokens = [token for token in tokens if token.strip() != '']
    return tokens
