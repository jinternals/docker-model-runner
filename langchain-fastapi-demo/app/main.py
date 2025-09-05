from fastapi import FastAPI
from app.api.router import router

app = FastAPI(title="LangChain + FastAPI Demo")

app.include_router(router)

@app.get("/health")
def health():
    return {"status": "ok"}
