from conf import BEARER
import re
import requests
import json

def get_text(text):
    headers = {"Authorization": f"Bearer {BEARER}"}
    API_URL = "https://api-inference.huggingface.co/models/kplro/model_proga"
    def query(payload):
        data = json.dumps(payload)
        response = requests.request("POST", API_URL, headers=headers, data=data)
        return json.loads(response.content.decode("utf-8"))
    data = query({"inputs": text,
           "parameters": {"temperature": 1.5,
                          "top_k": 2,
                          "do_sample": True,
                          "top_p": 0.9,
                          "max_new_tokens": 200,
                          "repetition_penalty":25},
           "options": {"wait_for_model": True,
                       "use_cache": False}
                 })
    generated_text = data[0]['generated_text']
    if '.' in generated_text:
        out_text = re.search(r'.*\.',generated_text).group()
    else:
        out_text = generated_text
    
    return out_text