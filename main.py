from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok", "service": "ml-sidecar"}

@app.get("/health")
def health():
    return {"healthy": True}
