import torch
from transformers import pipeline
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
import os
from langchain import PromptTemplate, LLMChain

# specify chat server
# HOST = 'localhost'
HOST = "127.0.0.1"
# PORT = 8001
PORT = 1024

URL = f'http://{HOST}:{PORT}'

# model_name = "databricks/dolly-v2-12b"
# model_name = "models/dolly-v2-7b"
# model_name = "kunishou/databricks-dolly-15k-ja"

# current_path = os.path.dirname(os.path.abspath(__file__))
# generate_text = pipeline(model=model_name,
#                          torch_dtype=torch.bfloat16,
#                          trust_remote_code=True,
#                          device_map="auto")

# from langchain.llms import RWKV
# # LLMの準備
# llm = RWKV(
#     model="./models/RWKV-4-Raven-14B-v9-Eng99-20230412-ctx8192.pth", 
#     # model="./models/RWKV-4-Raven-14B-v8-EngAndMore-20230408-ctx4096.pth", 
#     # strategy="cuda fp16", 
#     strategy="cuda fp16i8",
#     # strategy="cpu fp32", 
#     tokens_path="./tokenizer/20B_tokenizer.json",
#     temperature=1.0,
# )

app = FastAPI()


# Remove CORS restrictions (if needed)
# from fastapi.middleware.cors import CORSMiddleware
# origins = [
#     f'http://{HOST}',
# ]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


@app.get("/chat_api")
async def chat(text: str = ""):
    generated_text = 'hello'
    # res = generate_text(text)
    # generated_text = res[0]["generated_text"]
    
    # generated_text = llm(generate_prompt(text))
    
    reply = generated_text.replace('\n', '<br>')
    print(f'input:{text} reply:{reply}')

    outJson = {
        "output": [
            {
                "type": "text",
                "value": reply
            }
        ]
    }
    return outJson


app.mount("/", StaticFiles(directory="html", html=True), name="html")

def start_server():
    uvicorn.run(app, host=HOST, port=PORT)
    # uvicorn.run(app, host=HOST, port=PORT, log_level="info")


def main():
    start_server()

    # When you want to open a browser at the same time
    # Use thread(if needed)
    # import threading
    # import webbrowser
    # threading.Thread(target=start_server).start()
    # webbrowser.open(URL, new=0, autoraise=True)


if __name__ == "__main__":
    main()
