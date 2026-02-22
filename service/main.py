from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title="marketplace-health-service", version="0.1.0")


@app.get("/health")
def health():
    return JSONResponse(status_code=200, content={"status": "ok"})


@app.get("/")
def root():
    return {"service": "marketplace-health-service", "docs": "/docs", "health": "/health"}
