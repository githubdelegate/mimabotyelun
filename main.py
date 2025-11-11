from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/chat")
def read_chat():
    return {"Hello": "Chat"}

# 如果你需要加更多路由，就在这儿扩展，就跟搭积木似的

# 这块儿加给Vercel用的，就跟点火启动似的
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)